(function(){
  function setLang(l){
    document.getElementById('lang-nl').hidden=(l!=='nl');
    document.getElementById('lang-en').hidden=(l!=='en');
    document.documentElement.lang=l;
    try{localStorage.setItem('lang',l)}catch(e){}
  }
  document.querySelectorAll('.langbtn').forEach(function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-set'));window.scrollTo(0,0)})});
  var saved=null; try{saved=localStorage.getItem('lang')}catch(e){}
  if(location.hash==='#en') saved='en';
  if(saved==='en') setLang('en');

  var lb=document.getElementById('lb'), im=document.getElementById('lbimg'), cap=document.getElementById('lbcap');
  document.querySelectorAll('[data-full]').forEach(function(b){
    b.addEventListener('click',function(){
      im.src=b.dataset.full; im.alt=(b.querySelector('img')||{}).alt||''; cap.textContent=b.dataset.cap||'';
      if(lb.showModal) lb.showModal();
    });
  });
  lb.addEventListener('click',function(e){ if(e.target===lb) lb.close(); });

  document.querySelectorAll('.copybtn').forEach(function(c){
    c.addEventListener('click',function(){
      var code=c.parentNode.querySelector('.mail'); var t=code.textContent;
      function sel(){ var r=document.createRange(); r.selectNodeContents(code); var s=getSelection(); s.removeAllRanges(); s.addRange(r); }
      var done=function(){c.textContent=c.dataset.copied;setTimeout(function(){c.textContent=c.dataset.copy},1600)};
      try{ navigator.clipboard.writeText(t).then(done,sel); }catch(e){ sel(); }
    });
  });
})();
