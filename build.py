WA="528140274770"
def wa(t): 
    import urllib.parse; return f"https://wa.me/{WA}?text="+urllib.parse.quote(t)
WAMAIN=wa("Hola Alfonso, vi tu página y quiero información")
def head(title,desc,path,extra=""):
    return f'''<!doctype html><html lang="es-MX"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="https://santinialfonso.com{path}">
<meta property="og:type" content="website"><meta property="og:locale" content="es_MX">
<meta property="og:site_name" content="Santini Alfonso"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="https://santinialfonso.com{path}">
<meta property="og:image" content="https://santinialfonso.com/assets/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Santini Alfonso: bots de WhatsApp, agenda de citas y automatización para empresas en Monterrey">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#0f766e"><link rel="stylesheet" href="/assets/styles.css">{extra}</head><body>
<a class="skip" href="#main">Saltar al contenido</a>
<header class="top"><div class="wrap"><a class="logo" href="/">Santini<span>.</span>Alfonso</a>
<nav aria-label="Principal"><a href="/#servicios">Servicios</a><a href="/#demos">Demos</a><a href="/#precios">Precios</a><a href="/#contacto">Contacto</a>
<a class="btn btn-wa btn-sm" href="{WAMAIN}" rel="noopener">WhatsApp</a></nav></div></header>'''
FOOT=f'''<footer><div class="wrap"><div><strong>Santini Alfonso</strong><br>Automatización y bots para empresas · Monterrey, N.L.<br>WhatsApp <a href="{WAMAIN}">81 4027 4770</a></div>
<ul aria-label="Legal"><li><a href="/privacidad/">Aviso de privacidad</a></li><li><a href="/terminos/">Términos</a></li><li><a href="/eliminacion-datos/">Eliminación de datos</a></li></ul>
<ul aria-label="Redes"><li><a href="https://www.instagram.com/santini_alfonsobot" rel="noopener">Instagram</a></li><li><a href="https://www.facebook.com/share/18MhQXJnYr/" rel="noopener">Facebook</a></li><li><a href="https://www.tiktok.com/@santinialfonso" rel="noopener">TikTok</a></li><li><a href="https://x.com/santinialfonso1" rel="noopener">X</a></li><li><a href="https://www.linkedin.com/in/alfonso-santini-delgado-a51657326" rel="noopener">LinkedIn</a></li></ul>
<div style="width:100%">© 2026 Santini Alfonso</div></div></footer>
<a class="wa-float" href="{WAMAIN}" rel="noopener" aria-label="Escríbeme por WhatsApp">💬 WhatsApp</a>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookies"><p style="margin:0 0 10px">Uso cookies de medición (Google Analytics) para saber cuántas personas visitan la página. ¿Aceptas?</p>
<button class="btn btn-wa btn-sm" id="ck-ok">Aceptar</button> <button class="btn btn-ghost btn-sm" id="ck-no">No, gracias</button> <a href="/privacidad/">Más info</a></div>
<script src="/assets/site.js" defer></script></body></html>'''

svc=[("💬","Bot de WhatsApp","Contesta precios, horarios y dudas al instante, 24/7, con la API oficial de Meta. Cuando hace falta, te pasa la conversación con el resumen."),
("📷","Bots de Instagram y Facebook","Responde mensajes directos y comentarios con la misma información, y lleva a la persona a WhatsApp o a tu agenda."),
("📅","Página con agenda de citas","Tu cliente escoge servicio, persona, día y hora libre. Las citas no chocan y le llega su recordatorio."),
("📞","Agente de voz","Contesta las llamadas que hoy se pierden, da la información básica, toma el recado o aparta la cita."),
("📊","Paneles","Ves en un solo lugar citas, mensajes y clientes del día, sin abrir cinco apps."),
("⚙️","Automatización de procesos","Lo que haces a mano y se repite: recordatorios, cobros, reportes, pedir reseñas, pasar datos de un lado a otro.")]
prices=[("Página con agenda de citas","$6,400","pago único","Hosting y dominio aparte."),
("Bot de WhatsApp","$6,400","+ $2,000/mes","Mensajes de Meta aparte, según uso."),
("Bots de Instagram y Facebook","$6,400","+ $2,000/mes","Si ya tienes el de WhatsApp, se cotiza como extensión."),
("Agente de voz","$11,200","+ $2,800/mes","Minutos de llamada aparte, según uso."),
("Panel","$14,400","pago único","Depende de cuántas fuentes de datos conecte."),
("Automatización","$2,000","+ $650/mes por flujo","Licencias de terceros aparte, si aplican.")]
idx=head("Santini Alfonso · Bots de WhatsApp, agenda de citas y automatización en Monterrey","Bots de WhatsApp, Instagram y Facebook, agenda de citas, agentes de voz, paneles y automatización para empresas de Monterrey. Pruebas en vivo y diagnóstico sin costo.","/")
idx+=f'''<main id="main">
<section class="hero"><div class="wrap"><div><span class="eyebrow">Automatización para empresas · Monterrey</span>
<h1>Tu empresa contesta, agenda y da seguimiento aunque tú estés ocupado.</h1>
<p class="lead">Bots de WhatsApp, Instagram y Facebook, agenda de citas, agentes de voz y automatizaciones para empresas de Monterrey. Te lo enseño funcionando antes de que pagues.</p>
<div class="cta-row"><a class="btn btn-wa" href="{WAMAIN}" rel="noopener">💬 Escríbeme por WhatsApp</a><a class="btn btn-ghost" href="#demos">Ver demos en vivo</a></div></div>
<div><div class="phone" role="img" aria-label="Ejemplo de conversación con un bot de WhatsApp que agenda una cita"><div class="screen"><div class="chat-h">Tu empresa · en línea</div>
<div class="msg out">Hola, ¿tienen lugar el sábado para corte?</div><div class="msg in">¡Hola! Sí 🙌 El sábado tengo libre a las 10:00, 12:30 y 16:00. ¿Cuál te aparto?</div>
<div class="msg out">12:30</div><div class="msg in">Listo ✅ Quedaste el sábado a las 12:30. Te recuerdo un día antes.</div></div></div><p class="note">Conversación de ejemplo</p></div></div></section>

<section class="alt"><div class="wrap"><h2>¿Te suena esto?</h2><ul class="pain">
<li>Te escriben por WhatsApp, Instagram, Facebook y teléfono, y algún mensaje se queda sin respuesta.</li>
<li>Contestas lo mismo (precio, horario, ubicación) muchas veces al día.</li>
<li>Dos clientes quieren a la misma persona a la misma hora y las citas chocan.</li>
<li>Suena el teléfono cuando estás atendiendo y esa venta se va.</li></ul>
<p class="lead">Eso se arregla con herramientas sencillas, bien conectadas a cómo ya trabajas.</p></div></section>

<section id="servicios"><div class="wrap"><span class="eyebrow">Servicios</span><h2>Lo que hago por tu empresa</h2>
<div class="grid g3">{"".join(f'<article class="card"><span class="ico" aria-hidden="true">{i}</span><h3>{t}</h3><p>{d}</p></article>' for i,t,d in svc)}</div>
<p class="fine" style="margin-top:18px">Ideal para estéticas, barberías, spas, consultorios, talleres y empresas de servicio donde un mensaje sin contestar es un cliente perdido.</p></div></section>

<section id="demos" class="alt demo"><div class="wrap"><span class="eyebrow">Proyectos de muestra</span><h2>Pruébalo tú mismo</h2>
<p class="lead">Son demos reales que puedes tocar. No son clientes ni resultados: son ejemplos de lo que armo.</p>
<div class="grid g2">
<article class="card"><span class="tag">Demo</span><h3>Agenda para estilista</h3><p>Muestra hecha para una estilista. Escoges servicio, día y hora libre; la hora se aparta y ya no aparece para nadie más. El resumen llega por WhatsApp.</p><p style="margin-top:14px"><a class="btn btn-ghost btn-sm" href="/demos/lian/">Abrir la demo →</a></p></article>
<article class="card"><span class="tag">Ejemplo</span><h3>Propuesta para un spa con 2 sucursales</h3><p>Un solo WhatsApp para las dos sucursales, agenda por terapeuta sin choques, recordatorio un día antes y reporte diario para la gerente.</p><p style="margin-top:14px"><a class="btn btn-ghost btn-sm" href="/demos/spa/">Ver el ejemplo →</a></p></article></div></div></section>

<section id="como"><div class="wrap"><span class="eyebrow">Cómo trabajo</span><h2>Simple y sin letras chiquitas</h2><ol class="steps">
<li><h3>Diagnóstico gratis</h3><p>30 minutos para ver dónde se te van clientes y qué conviene automatizar primero. Te quedas con las ideas aunque no trabajemos juntos.</p></li>
<li><h3>Demo con tus datos</h3><p>Te armo una prueba con tus servicios y horarios para que la veas funcionar.</p></li>
<li><h3>Piloto de 30 días</h3><p>Lo usamos con clientes reales y ajustamos lo necesario.</p></li>
<li><h3>Funcionando y con soporte</h3><p>Te lo dejo listo y te respondo cuando algo falle o quieras cambiar algo.</p></li></ol></div></section>

<section id="precios" class="alt"><div class="wrap"><span class="eyebrow">Precios</span><h2>Precios desde</h2>
<p class="lead">Precios de entrada en pesos. El precio final depende de lo que necesites; te lo digo por escrito antes de empezar.</p>
<p class="fine">Precios sujetos a cambio.</p>
<div class="grid g3">{"".join(f'<article class="card"><h3>{t}</h3><p class="price">desde {p} <small>{m}</small></p><p class="fine">{n}</p></article>' for t,p,m,n in prices)}</div>
<details style="margin-top:20px"><summary>¿Por qué hay mensualidad?</summary><p>Porque el bot trabaja todos los días: la mensualidad cubre la plataforma, el servidor, el uso de la inteligencia artificial, los ajustes y el soporte. Lo que cobra Meta por mensaje o la compañía por minuto de llamada se paga según el uso.</p></details></div></section>

<section id="sobre-mi"><div class="wrap about"><picture><source srcset="/assets/alfonso.webp" type="image/webp"><img src="/assets/alfonso.jpg" alt="Alfonso Santini, consultor de automatización en Monterrey" width="864" height="1152" decoding="async" class="avatar photo"></picture>
<div><span class="eyebrow">Sobre mí</span><h2>Hola, soy Alfonso.</h2><p class="lead">Vivo en Monterrey y armo herramientas para que las empresas locales no pierdan clientes por no contestar a tiempo. Te explico todo sin tecnicismos, te enseño la demo antes de cobrarte y me quedo contigo después de entregar.</p></div></div></section>

<section class="alt" id="faq"><div class="wrap"><h2>Preguntas frecuentes</h2>
<details><summary>¿Es WhatsApp oficial?</summary><p>Sí. Trabajo solo con la plataforma oficial de WhatsApp Business de Meta, para que tu número no corra riesgo de bloqueo.</p></details>
<details><summary>¿Tengo que cambiar el sistema que ya uso?</summary><p>No necesariamente. Primero veo qué usas hoy y, si se puede, lo conecto en lugar de reemplazarlo.</p></details>
<details><summary>¿Qué pasa con los datos de mis clientes?</summary><p>Son tuyos. Solo se usan para darte el servicio y puedes pedir que se borren. Lee el <a href="/privacidad/">aviso de privacidad</a>.</p></details>
<details><summary>¿Puedo cancelar la mensualidad?</summary><p>Sí, avisando con 30 días. Sin plazos forzosos.</p></details>
<details><summary>¿Cuánto tarda?</summary><p>Una demo, en pocos días. Lo demás depende del alcance; te doy la fecha por escrito antes de empezar.</p></details></div></section>

<section id="contacto"><div class="wrap grid g2"><div><span class="eyebrow">Contacto</span><h2>Platícame de tu empresa o negocio</h2>
<p class="lead">La forma más rápida es WhatsApp. Si prefieres, llena el formulario y se abre WhatsApp con tu mensaje listo.</p>
<p><a class="btn btn-wa" href="{WAMAIN}" rel="noopener">💬 81 4027 4770</a></p></div>
<form id="f" class="card" novalidate><div class="hp" aria-hidden="true"><label for="web">No llenar</label><input id="web" name="web" tabindex="-1" autocomplete="off"></div>
<label for="n">Tu nombre</label><input id="n" name="n" required minlength="2" maxlength="60" autocomplete="name"><div class="err" id="e-n"></div>
<label for="g">Tipo de empresa o negocio</label><input id="g" name="g" required minlength="2" maxlength="60" placeholder="Ej. estética, taller, consultorio"><div class="err" id="e-g"></div>
<label for="s">¿Qué te interesa?</label><select id="s" name="s" required><option value="">Elige una opción</option>{"".join(f"<option>{t}</option>" for _,t,_ in svc)}<option>No sé, quiero el diagnóstico</option></select><div class="err" id="e-s"></div>
<label for="m">Cuéntame en breve (opcional)</label><textarea id="m" name="m" rows="3" maxlength="400"></textarea>
<p class="fine">Al enviar aceptas el <a href="/privacidad/">aviso de privacidad</a>. Este formulario no guarda datos: solo abre WhatsApp con tu mensaje.</p>
<button class="btn btn-wa" type="submit">Enviar por WhatsApp</button><div class="err" id="e-f" role="alert"></div></form></div></section>
</main>'''+FOOT
open("index.html","w").write(idx)

def legal(path,title,body):
    open(path.strip("/")+"/index.html","w").write(head(title+" · Santini Alfonso",title+" de santinialfonso.com",path)+f'<main id="main"><section><div class="wrap legal"><h1>{title}</h1><p class="fine">Última actualización: 23 de octubre de 2026</p>{body}</div></section></main>'+FOOT)
legal("/privacidad/","Aviso de privacidad",f'''<p><strong>[REVISAR: borrador para validar con un abogado antes de publicar.]</strong></p>
<h2>Responsable</h2><p>Alfonso Santini Delgado, con domicilio en Monterrey, Nuevo León, México [DOMICILIO PARA OÍR Y RECIBIR NOTIFICACIONES], es responsable del tratamiento de tus datos personales conforme a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares.</p>
<h2>Datos que tratamos</h2><p>Nombre, teléfono o WhatsApp, tipo de empresa o negocio y lo que nos escribas al contactarnos. No pedimos datos sensibles.</p>
<h2>Para qué</h2><p>Responder tu solicitud, enviarte una propuesta y darte el servicio contratado. De forma secundaria, y solo si aceptas cookies, medir visitas a la página con Google Analytics.</p>
<h2>Bots que operamos para nuestros clientes</h2><p>Cuando operamos un bot para una empresa, esa empresa es la responsable de los datos de sus clientes y nosotros actuamos como encargados, solo bajo sus instrucciones.</p>
<h2>Transferencias</h2><p>Usamos proveedores para funcionar (por ejemplo Meta/WhatsApp, Google y el alojamiento de esta página). No vendemos tus datos.</p>
<h2>Derechos ARCO</h2><p>Puedes acceder, rectificar, cancelar u oponerte al uso de tus datos, o revocar tu consentimiento, escribiendo por WhatsApp al 81 4027 4770 o a [CORREO DE CONTACTO]. Respondemos en máximo 20 días hábiles.</p>
<h2>Cookies</h2><p>Esta página solo usa cookies de medición si das clic en «Aceptar». Puedes borrarlas desde tu navegador.</p>
<h2>Cambios</h2><p>Publicaremos cualquier cambio en esta misma página.</p>''')
legal("/terminos/","Términos y condiciones",'''<p><strong>[REVISAR: borrador para validar con un abogado antes de publicar.]</strong></p>
<h2>Servicios</h2><p>Los servicios, alcance, precio y plazos de cada proyecto se acuerdan por escrito antes de empezar. Los precios publicados son de referencia («desde») y están en pesos mexicanos.</p>
<h2>Pagos</h2><p>[DEFINIR: anticipo, forma de pago y si se emite factura.] Los costos de terceros (Meta, minutos de llamada, dominio, hosting, licencias) se pagan según el uso y se informan antes.</p>
<h2>Mensualidades</h2><p>Se pueden cancelar avisando con 30 días. Al cancelar te entregamos tu información.</p>
<h2>Demos</h2><p>Las demos de esta página son ejemplos y no representan clientes ni resultados reales.</p>
<h2>Responsabilidad</h2><p>Hacemos lo razonable para que todo funcione, pero no respondemos por caídas o cambios de servicios de terceros como WhatsApp o Meta.</p>
<h2>Contacto</h2><p>WhatsApp 81 4027 4770.</p>''')
legal("/eliminacion-datos/","Eliminación de datos",'''<p>Si conversaste con un bot operado por nosotros (WhatsApp, Instagram o Facebook) o nos dejaste tus datos, puedes pedir que se borren.</p>
<h2>Cómo pedirlo</h2><ol><li>Escribe por WhatsApp al 81 4027 4770 con el mensaje «Borrar mis datos».</li><li>Indica el número o usuario con el que nos escribiste y, si aplica, la empresa o negocio.</li><li>Confirmamos tu identidad y borramos tus datos en un máximo de 30 días.</li></ol>
<p>Te avisamos cuando quede hecho. Lo que Meta guarda en sus propias apps se rige por sus políticas.</p>''')
open("404.html","w").write(head("Página no encontrada · Santini Alfonso","Esta página no existe.","/404.html",'<meta name="robots" content="noindex">')+f'<main id="main"><section><div class="wrap" style="text-align:center"><h1>Ups, esta página no existe.</h1><p class="lead" style="margin:0 auto">Pero tu empresa sí puede contestar a tiempo.</p><div class="cta-row" style="justify-content:center"><a class="btn btn-ghost" href="/">Ir al inicio</a><a class="btn btn-wa" href="{WAMAIN}">💬 WhatsApp</a></div></div></section></main>'+FOOT)
