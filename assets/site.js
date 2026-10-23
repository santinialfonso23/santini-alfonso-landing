// GA4: pon aquí tu ID (ej. "G-XXXXXXXXXX"). Vacío = no se carga nada y no sale el banner de cookies.
var GA4_ID = "";
(function(){
  function loadGA(){var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+GA4_ID;document.head.appendChild(s);
    window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config',GA4_ID,{anonymize_ip:true});}
  var c=document.getElementById('cookie');
  if(GA4_ID&&c){var v=localStorage.getItem('ck');
    if(v==='1')loadGA();else if(v!=='0'){c.style.display='block';
      document.getElementById('ck-ok').onclick=function(){localStorage.setItem('ck','1');c.style.display='none';loadGA();};
      document.getElementById('ck-no').onclick=function(){localStorage.setItem('ck','0');c.style.display='none';};}}
  var f=document.getElementById('f');if(!f)return;var t0=Date.now();
  f.addEventListener('submit',function(e){e.preventDefault();
    var ok=true,F=function(id,msg,cond){document.getElementById('e-'+id).textContent=cond?'':msg;if(!cond)ok=false;};
    var n=f.n.value.trim(),g=f.g.value.trim(),s=f.s.value,m=f.m.value.trim();
    F('n','Escribe tu nombre (mínimo 2 letras).',n.length>=2&&n.length<=60&&!/https?:|<|>/i.test(n));
    F('g','Dime qué tipo de negocio tienes.',g.length>=2&&g.length<=60&&!/https?:|<|>/i.test(g));
    F('s','Elige una opción.',!!s);
    var ef=document.getElementById('e-f');ef.textContent='';
    if(f.web.value||Date.now()-t0<3000||/https?:\/\//i.test(m)){ef.textContent='No se pudo enviar. Escríbeme directo por WhatsApp.';return;}
    if(!ok)return;
    var txt='Hola Alfonso, soy '+n+'. Tengo '+g+' y me interesa: '+s+'.'+(m?' '+m:'');
    window.open('https://wa.me/528140274770?text='+encodeURIComponent(txt),'_blank','noopener');});
})();
