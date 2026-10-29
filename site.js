(function(){
  function setLang(l){
    document.getElementById('lang-nl').hidden=(l!=='nl');
    document.getElementById('lang-en').hidden=(l!=='en');
    document.documentElement.lang=l;
    try{localStorage.setItem('lang',l)}catch(e){}
    observe();
  }
  document.querySelectorAll('.langbtn').forEach(function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-set'));window.scrollTo(0,0)})});
  var saved=null; try{saved=localStorage.getItem('lang')}catch(e){}
  if(location.hash==='#en') saved='en';

  // reveal on scroll
  var io='IntersectionObserver' in window ? new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  },{rootMargin:'0px 0px -8% 0px',threshold:.08}) : null;
  function observe(){
    document.querySelectorAll('.lang:not([hidden]) .reveal:not(.in)').forEach(function(el){ if(io) io.observe(el); else el.classList.add('in'); });
  }
  if(saved==='en') setLang('en'); else observe();

  // project dialog
  var pm=document.getElementById('pm');
  document.querySelectorAll('[data-project]').forEach(function(c){
    c.addEventListener('click',function(){
      var d=JSON.parse(c.getAttribute('data-project'));
      document.getElementById('pm-t').innerHTML=d.t;
      document.getElementById('pm-g').innerHTML=d.g;
      document.getElementById('pm-p').innerHTML=d.p;
      var l=document.getElementById('pm-l');
      if(d.l){ l.href=d.l; l.textContent=d.v+' ↗'; l.hidden=false; } else { l.hidden=true; }
      var box=document.getElementById('pm-i'); box.innerHTML='';
      d.i.forEach(function(im){
        var img=document.createElement('img'); img.src=im[0]; img.width=im[1]; img.height=im[2]; img.alt=''; img.loading='lazy'; box.appendChild(img);
      });
      if(pm.showModal){ pm.showModal(); pm.scrollTop=0; }
    });
  });
  pm.addEventListener('click',function(e){ if(e.target===pm) pm.close(); });

  document.querySelectorAll('.copybtn').forEach(function(c){
    c.addEventListener('click',function(){
      var t=c.parentNode.querySelector('.mail').textContent;
      var done=function(){c.textContent=c.dataset.copied;setTimeout(function(){c.textContent=c.dataset.copy},1600)};
      try{ navigator.clipboard.writeText(t).then(done,function(){}); }catch(e){}
    });
  });
})();
