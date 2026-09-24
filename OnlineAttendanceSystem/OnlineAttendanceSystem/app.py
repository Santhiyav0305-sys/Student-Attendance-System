from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from functools import wraps
from datetime import date
app=Flask(__name__); app.secret_key='attendance_secret'; DB='database.db'
def db():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def init():
 c=db(); c.executescript('''CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL,department TEXT NOT NULL,phone TEXT); CREATE TABLE IF NOT EXISTS teachers(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL,subject TEXT NOT NULL); CREATE TABLE IF NOT EXISTS attendance(id INTEGER PRIMARY KEY AUTOINCREMENT,student_id INTEGER NOT NULL,date TEXT NOT NULL,status TEXT NOT NULL,UNIQUE(student_id,date),FOREIGN KEY(student_id) REFERENCES students(id));'''); c.commit(); c.close()
def login_required(f):
 @wraps(f)
 def w(*a,**k): return f(*a,**k) if session.get('logged_in') else redirect(url_for('login'))
 return w
@app.route('/',methods=['GET','POST'])
def login():
 if session.get('logged_in'): return redirect(url_for('dashboard'))
 if request.method=='POST':
  if request.form.get('username')=='admin' and request.form.get('password')=='admin123': session['logged_in']=1; return redirect(url_for('dashboard'))
  flash('Invalid username or password','error')
 return render_template('login.html')
@app.route('/dashboard')
@login_required
def dashboard():
 c=db(); s=c.execute('SELECT COUNT(*) n FROM students').fetchone()['n']; t=c.execute('SELECT COUNT(*) n FROM teachers').fetchone()['n']; p=c.execute("SELECT COUNT(*) n FROM attendance WHERE status='Present'").fetchone()['n']; a=c.execute("SELECT COUNT(*) n FROM attendance WHERE status='Absent'").fetchone()['n']; today=date.today().isoformat(); tp=c.execute("SELECT COUNT(*) n FROM attendance WHERE date=? AND status='Present'",(today,)).fetchone()['n']; ta=c.execute("SELECT COUNT(*) n FROM attendance WHERE date=? AND status='Absent'",(today,)).fetchone()['n']; c.close(); return render_template('dashboard.html',students=s,teachers=t,present=p,absent=a,percentage=round(p*100/(p+a),1) if p+a else 0,today=today,today_present=tp,today_absent=ta)
@app.route('/students')
@login_required
def students():
 c=db(); rows=c.execute('SELECT * FROM students ORDER BY id DESC').fetchall(); c.close(); return render_template('students.html',students=rows)
@app.route('/add_student',methods=['GET','POST'])
@login_required
def add_student():
 if request.method=='POST':
  c=db(); c.execute('INSERT INTO students(name,email,department,phone) VALUES(?,?,?,?)',(request.form['name'],request.form['email'],request.form['department'],request.form.get('phone',''))); c.commit(); c.close(); flash('Student added successfully','success'); return redirect(url_for('students'))
 return render_template('add_student.html')
@app.route('/edit_student/<int:id>',methods=['GET','POST'])
@login_required
def edit_student(id):
 c=db(); s=c.execute('SELECT * FROM students WHERE id=?',(id,)).fetchone()
 if request.method=='POST': c.execute('UPDATE students SET name=?,email=?,department=?,phone=? WHERE id=?',(request.form['name'],request.form['email'],request.form['department'],request.form.get('phone',''),id)); c.commit(); c.close(); flash('Student updated','success'); return redirect(url_for('students'))
 c.close(); return render_template('edit_student.html',student=s)
@app.post('/delete_student/<int:id>')
@login_required
def delete_student(id):
 c=db(); c.execute('DELETE FROM attendance WHERE student_id=?',(id,)); c.execute('DELETE FROM students WHERE id=?',(id,)); c.commit(); c.close(); return redirect(url_for('students'))
@app.route('/student_profile/<int:id>')
@login_required
def profile(id):
 c=db(); s=c.execute('SELECT * FROM students WHERE id=?',(id,)).fetchone(); r=c.execute('SELECT date,status FROM attendance WHERE student_id=? ORDER BY date DESC',(id,)).fetchall(); c.close(); p=sum(x['status']=='Present' for x in r); return render_template('student_profile.html',student=s,records=r,present=p,absent=len(r)-p,percentage=round(p*100/len(r),1) if r else 0)
@app.route('/teachers')
@login_required
def teachers():
 c=db(); rows=c.execute('SELECT * FROM teachers ORDER BY id DESC').fetchall(); c.close(); return render_template('teachers.html',teachers=rows)
@app.route('/add_teacher',methods=['GET','POST'])
@login_required
def add_teacher():
 if request.method=='POST':
  c=db(); c.execute('INSERT INTO teachers(name,email,subject) VALUES(?,?,?)',(request.form['name'],request.form['email'],request.form['subject'])); c.commit(); c.close(); return redirect(url_for('teachers'))
 return render_template('add_teacher.html')
@app.route('/edit_teacher/<int:id>',methods=['GET','POST'])
@login_required
def edit_teacher(id):
 c=db(); t=c.execute('SELECT * FROM teachers WHERE id=?',(id,)).fetchone()
 if request.method=='POST': c.execute('UPDATE teachers SET name=?,email=?,subject=? WHERE id=?',(request.form['name'],request.form['email'],request.form['subject'],id)); c.commit(); c.close(); return redirect(url_for('teachers'))
 c.close(); return render_template('edit_teacher.html',teacher=t)
@app.post('/delete_teacher/<int:id>')
@login_required
def delete_teacher(id):
 c=db(); c.execute('DELETE FROM teachers WHERE id=?',(id,)); c.commit(); c.close(); return redirect(url_for('teachers'))
@app.route('/attendance',methods=['GET','POST'])
@login_required
def attendance():
 c=db(); students=c.execute('SELECT * FROM students ORDER BY name').fetchall(); d=request.args.get('date',date.today().isoformat())
 if request.method=='POST':
  d=request.form['date']
  for s in students:
   st=request.form.get(f'status_{s["id"]}')
   if st: c.execute("INSERT INTO attendance(student_id,date,status) VALUES(?,?,?) ON CONFLICT(student_id,date) DO UPDATE SET status=excluded.status",(s['id'],d,st))
  c.commit(); c.close(); flash('Attendance saved','success'); return redirect(url_for('attendance',date=d))
 old={r['student_id']:r['status'] for r in c.execute('SELECT student_id,status FROM attendance WHERE date=?',(d,)).fetchall()}; c.close(); return render_template('attendance.html',students=students,date=d,old=old)
@app.route('/attendance_history')
@login_required
def history():
 c=db(); rows=c.execute('SELECT a.date,s.name,s.department,a.status FROM attendance a JOIN students s ON s.id=a.student_id ORDER BY a.date DESC,s.name').fetchall(); c.close(); return render_template('attendance_history.html',records=rows)
@app.route('/reports')
@login_required
def reports():
 c=db(); rows=c.execute("SELECT s.name,s.department,COUNT(a.id) total,COALESCE(SUM(a.status='Present'),0) present,COALESCE(SUM(a.status='Absent'),0) absent FROM students s LEFT JOIN attendance a ON a.student_id=s.id GROUP BY s.id ORDER BY s.name").fetchall(); c.close(); return render_template('reports.html',rows=rows)
@app.route('/about')
@login_required
def about(): return render_template('about.html')
@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))
init()
if __name__=='__main__': app.run(debug=True)
