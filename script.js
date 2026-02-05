document.addEventListener('DOMContentLoaded',()=>{
  const input=document.getElementById('search');
  const cards=Array.from(document.querySelectorAll('.card'));
  const toggle=document.getElementById('darkToggle');

  input?.addEventListener('input',()=>{
    const q=(input.value||'').toLowerCase();
    cards.forEach(c=>{
      const title=c.dataset.title.toLowerCase();
      const genre=(c.dataset.genre||'').toLowerCase();
      c.style.display=(title.includes(q)||genre.includes(q))? 'block':'none';
    });
  });

  toggle?.addEventListener('click',()=>{
    document.body.classList.toggle('dark');
    toggle.textContent=document.body.classList.contains('dark')? 'Modo Claro':'Modo Escuro';
  });
});