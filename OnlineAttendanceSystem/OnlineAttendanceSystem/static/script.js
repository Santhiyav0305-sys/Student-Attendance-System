function filterTable(){const q=document.getElementById('search').value.toLowerCase();document.querySelectorAll('table tr').forEach((r,i)=>{if(i)r.style.display=r.innerText.toLowerCase().includes(q)?'':'none'})}
setTimeout(()=>document.querySelectorAll('.flash').forEach(x=>x.remove()),3500);
