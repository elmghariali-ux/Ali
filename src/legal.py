"""ZAYA legal pages (EN + ES). Filled by build.py from OWNER below.

Owner details are required by Spain's LSSI (art. 10) and the GDPR (art. 13).
While a value is empty the build marks it as pending; never publish pending pages.
"""

OWNER = {
    "name": "",        # full legal name of the person (or company) running ZAYA
    "id": "",          # DNI / NIE (or NIF/CIF for a company)
    "address": "",     # postal address for notifications
    "email": "zaya.ritual@gmail.com",
}
UPDATED_EN = "20 October 2026"
UPDATED_ES = "20 de octubre de 2026"

PAGES = {}

PAGES["legal"] = {
    "title": "Legal notice — ZAYA",
    "desc": "Legal notice for zayaritual.com, the website of ZAYA, an Afro House ritual in Barcelona.",
    "h_en": "Legal notice", "h_es": "Aviso legal",
    "en": """
<h2>1. Who runs this website</h2>
<p>In accordance with Spanish Law 34/2002 on information society services and e-commerce (LSSI-CE), the owner of zayaritual.com is:</p>
<dl class="id">
  <div><dt>Owner</dt><dd>{name}</dd></div>
  <div><dt>DNI / NIE</dt><dd>{id}</dd></div>
  <div><dt>Address</dt><dd>{address}</dd></div>
  <div><dt>Email</dt><dd><a href="mailto:{email}">{email}</a></dd></div>
</dl>
<p>ZAYA is the trade name under which the owner organises Afro House events in Barcelona.</p>

<h2>2. Purpose of the website</h2>
<p>This website presents ZAYA and its events, and lets visitors request an invitation. Requesting an invitation does not guarantee one, and does not create any obligation to buy a ticket. Tickets, when offered, are sold through a ticketing platform under its own terms.</p>

<h2>3. Use of the website</h2>
<p>By using this website you agree to do so lawfully and in good faith, and not to damage it, interfere with its operation or misuse the invitation form. Event details (date, venue, line-up) may change; the information published here is given in good faith and may be updated without notice.</p>

<h2>4. Intellectual property</h2>
<p>The ZAYA name and identity, texts, photographs, films and design of this website belong to the owner or are used with the permission of their authors and rights holders. They may not be reproduced, distributed or publicly communicated without prior written permission, except to share links to this website or to share the personal invitation card the site generates for you.</p>

<h2>5. Links</h2>
<p>This website links to third-party sites such as Instagram. The owner is not responsible for their content or their privacy practices.</p>

<h2>6. Liability</h2>
<p>The owner works to keep the website available and accurate, but cannot guarantee uninterrupted access or the absence of errors, and is not liable for damage arising from use of the website, except where the law provides otherwise.</p>

<h2>7. Law and jurisdiction</h2>
<p>These terms are governed by Spanish law. Any dispute will be submitted to the courts of Barcelona, without prejudice to any right you have as a consumer to bring proceedings in the courts of your place of residence.</p>
""",
    "es": """
<h2>1. Titular del sitio web</h2>
<p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), el titular de zayaritual.com es:</p>
<dl class="id">
  <div><dt>Titular</dt><dd>{name}</dd></div>
  <div><dt>DNI / NIE</dt><dd>{id}</dd></div>
  <div><dt>Domicilio</dt><dd>{address}</dd></div>
  <div><dt>Correo</dt><dd><a href="mailto:{email}">{email}</a></dd></div>
</dl>
<p>ZAYA es el nombre comercial con el que el titular organiza eventos de Afro House en Barcelona.</p>

<h2>2. Finalidad del sitio web</h2>
<p>Este sitio web presenta ZAYA y sus eventos, y permite solicitar una invitación. Solicitar una invitación no garantiza recibirla ni obliga a comprar una entrada. Las entradas, cuando se ofrezcan, se venden a través de una plataforma de venta con sus propias condiciones.</p>

<h2>3. Uso del sitio web</h2>
<p>Al usar este sitio web te comprometes a hacerlo de forma lícita y de buena fe, sin dañarlo, alterar su funcionamiento ni hacer un uso indebido del formulario de invitación. Los detalles de los eventos (fecha, lugar, artistas) pueden cambiar; la información publicada se ofrece de buena fe y puede actualizarse sin previo aviso.</p>

<h2>4. Propiedad intelectual</h2>
<p>El nombre y la identidad de ZAYA, los textos, fotografías, vídeos y el diseño de este sitio web pertenecen al titular o se utilizan con permiso de sus autores y titulares de derechos. No pueden reproducirse, distribuirse ni comunicarse públicamente sin autorización previa por escrito, salvo para compartir enlaces a este sitio o la tarjeta de invitación personal que el sitio genera para ti.</p>

<h2>5. Enlaces</h2>
<p>Este sitio web enlaza con sitios de terceros como Instagram. El titular no es responsable de su contenido ni de sus prácticas de privacidad.</p>

<h2>6. Responsabilidad</h2>
<p>El titular procura que el sitio web esté disponible y sea exacto, pero no puede garantizar el acceso ininterrumpido ni la ausencia de errores, y no responde de los daños derivados de su uso, salvo en los casos previstos por la ley.</p>

<h2>7. Ley aplicable y jurisdicción</h2>
<p>Estas condiciones se rigen por la ley española. Cualquier controversia se someterá a los juzgados y tribunales de Barcelona, sin perjuicio del derecho que te corresponda como consumidor a acudir a los tribunales de tu domicilio.</p>
""",
}

PAGES["privacy"] = {
    "title": "Privacy policy — ZAYA",
    "desc": "How ZAYA handles the personal data you share when you request an invitation on zayaritual.com.",
    "h_en": "Privacy policy", "h_es": "Política de privacidad",
    "en": """
<p class="lede">You share very little with us, and we keep it that way. This page explains what we collect when you request an invitation, why, and the rights you have under the EU General Data Protection Regulation (GDPR) and Spain's data protection law (LOPDGDD).</p>

<h2>1. Who is responsible for your data</h2>
<dl class="id">
  <div><dt>Controller</dt><dd>{name}</dd></div>
  <div><dt>DNI / NIE</dt><dd>{id}</dd></div>
  <div><dt>Address</dt><dd>{address}</dd></div>
  <div><dt>Email</dt><dd><a href="mailto:{email}">{email}</a></dd></div>
</dl>

<h2>2. What we collect</h2>
<ul>
  <li><b>When you request an invitation:</b> your name, email and, if you choose to give them, your Instagram username and your answer to our question. We also record that you accepted this policy, when you did so, and whether you asked to hear about future nights.</li>
  <li><b>When you write to us:</b> your email address and whatever you include in your message.</li>
  <li><b>When you visit:</b> anonymous, aggregated audience statistics (see section 6). We do not use cookies.</li>
</ul>
<p>The story card the site creates for you is generated on your own device and is not sent to us.</p>

<h2>3. Why we use it, and on what legal basis</h2>
<ul>
  <li><b>To handle your invitation request</b> — to read it, decide on it, and contact you about the edition you asked for (your invitation, ticket link and the address of the night). Legal basis: your consent, and steps taken at your request before a possible purchase (GDPR art. 6.1.a and 6.1.b).</li>
  <li><b>To tell you about future ZAYA nights</b>, only if you tick that box. Legal basis: your consent (art. 6.1.a). You can withdraw it at any time, and every email lets you unsubscribe.</li>
  <li><b>To understand, in aggregate, how the site is used</b>. Legal basis: our legitimate interest in running and improving the site (art. 6.1.f). These statistics do not identify you.</li>
</ul>
<p>Every request is read by a person. We do not use automated decision-making or profiling.</p>

<h2>4. Who we share it with</h2>
<p>We never sell your data. We share it only with service providers who help us run the site and handle requests, and who act on our instructions:</p>
<ul>
  <li><b>Formspree, Inc.</b> (USA) — receives the form and forwards it to our inbox.</li>
  <li><b>Google</b> (Gmail) — the email inbox where requests arrive and from which we reply.</li>
  <li><b>Vercel Inc.</b> (USA) — hosts this website and provides the anonymous statistics.</li>
</ul>
<p>If you are invited, your name may be given to the venue's door team only to manage entry, and tickets are sold by a ticketing platform that will tell you about its own privacy terms. We may also disclose data where the law requires it.</p>

<h2>5. Transfers outside the European Union</h2>
<p>Some of these providers may process data in the United States. Those transfers are covered by the EU–US Data Privacy Framework where the provider is certified under it, or by the European Commission's Standard Contractual Clauses.</p>

<h2>6. Statistics, and no cookies</h2>
<p>We count visits with Vercel Web Analytics, which does not use cookies or store anything on your device. It records anonymous information such as the page visited, the referring site, country, device type and browser, and recognises a returning visit only through a temporary anonymous code that is discarded after 24 hours. See our <a href="/cookies">cookie statement</a>.</p>

<h2>7. How long we keep it</h2>
<ul>
  <li>Invitation requests: until the end of the edition you applied for and for up to 12 months afterwards, so we can consider you for the next night — or until you ask us to delete them sooner.</li>
  <li>News about future nights: until you unsubscribe or withdraw consent.</li>
</ul>
<p>After that we delete the data, or keep it blocked only for as long as the law requires to deal with possible claims.</p>

<h2>8. Your rights</h2>
<p>You can ask to access, correct or delete your data, to object to or restrict its use, to receive it in a portable format, and you can withdraw your consent at any time without affecting what was done before. Write to <a href="mailto:{email}?subject=Privacy">{email}</a> with “Privacy” in the subject. If you think we have not handled your data properly, you can complain to the Spanish Data Protection Agency (AEPD), <a href="https://www.aepd.es" target="_blank" rel="noopener">www.aepd.es</a>.</p>

<h2>9. Age</h2>
<p>ZAYA is for adults. You must be 18 or over to request an invitation. If we learn that a request comes from someone under 18, we delete it.</p>

<h2>10. Security and changes</h2>
<p>We take reasonable technical and organisational measures to protect your data. If this policy changes, we will publish the new version here with its date.</p>
""",
    "es": """
<p class="lede">Compartes muy poco con nosotros, y así queremos que siga siendo. Esta página explica qué datos recogemos cuando solicitas una invitación, para qué, y los derechos que te reconocen el Reglamento General de Protección de Datos (RGPD) y la Ley Orgánica 3/2018 (LOPDGDD).</p>

<h2>1. Responsable del tratamiento</h2>
<dl class="id">
  <div><dt>Responsable</dt><dd>{name}</dd></div>
  <div><dt>DNI / NIE</dt><dd>{id}</dd></div>
  <div><dt>Domicilio</dt><dd>{address}</dd></div>
  <div><dt>Correo</dt><dd><a href="mailto:{email}">{email}</a></dd></div>
</dl>

<h2>2. Qué datos recogemos</h2>
<ul>
  <li><b>Al solicitar una invitación:</b> tu nombre, tu correo y, si decides darlos, tu usuario de Instagram y tu respuesta a nuestra pregunta. También registramos que aceptaste esta política, cuándo, y si pediste recibir noticias de próximas noches.</li>
  <li><b>Si nos escribes:</b> tu correo y lo que incluyas en tu mensaje.</li>
  <li><b>Al visitar el sitio:</b> estadísticas de audiencia anónimas y agregadas (ver apartado 6). No usamos cookies.</li>
</ul>
<p>La tarjeta para stories que crea el sitio se genera en tu propio dispositivo y no se nos envía.</p>

<h2>3. Para qué los usamos y con qué base legal</h2>
<ul>
  <li><b>Gestionar tu solicitud de invitación</b>: leerla, decidir sobre ella y contactarte sobre la edición solicitada (invitación, enlace de entrada y dirección de la noche). Base legal: tu consentimiento y la aplicación de medidas precontractuales a petición tuya (art. 6.1.a y 6.1.b RGPD).</li>
  <li><b>Informarte de próximas noches de ZAYA</b>, solo si marcas esa casilla. Base legal: tu consentimiento (art. 6.1.a). Puedes retirarlo cuando quieras y cada correo incluye la opción de darte de baja.</li>
  <li><b>Conocer de forma agregada cómo se usa el sitio</b>. Base legal: nuestro interés legítimo en mantener y mejorar el sitio (art. 6.1.f). Estas estadísticas no te identifican.</li>
</ul>
<p>Cada solicitud la lee una persona. No tomamos decisiones automatizadas ni elaboramos perfiles.</p>

<h2>4. Con quién los compartimos</h2>
<p>Nunca vendemos tus datos. Solo los compartimos con proveedores que nos ayudan a mantener el sitio y gestionar las solicitudes, y que actúan siguiendo nuestras instrucciones (encargados del tratamiento):</p>
<ul>
  <li><b>Formspree, Inc.</b> (EE. UU.): recibe el formulario y lo reenvía a nuestro correo.</li>
  <li><b>Google</b> (Gmail): el buzón donde llegan las solicitudes y desde el que respondemos.</li>
  <li><b>Vercel Inc.</b> (EE. UU.): aloja este sitio web y ofrece las estadísticas anónimas.</li>
</ul>
<p>Si recibes una invitación, tu nombre podrá facilitarse al equipo de acceso del local únicamente para gestionar la entrada, y las entradas se venden a través de una plataforma que te informará de su propia política de privacidad. También podremos comunicar datos cuando la ley lo exija.</p>

<h2>5. Transferencias fuera de la Unión Europea</h2>
<p>Algunos de estos proveedores pueden tratar datos en Estados Unidos. Esas transferencias se amparan en el Marco de Privacidad de Datos UE–EE. UU. cuando el proveedor está certificado, o en las Cláusulas Contractuales Tipo de la Comisión Europea.</p>

<h2>6. Estadísticas, y sin cookies</h2>
<p>Contamos las visitas con Vercel Web Analytics, que no usa cookies ni guarda nada en tu dispositivo. Registra información anónima como la página visitada, el sitio de procedencia, el país, el tipo de dispositivo y el navegador, y solo reconoce una visita repetida mediante un código anónimo temporal que se elimina a las 24 horas. Consulta nuestra <a href="/cookies#es">política de cookies</a>.</p>

<h2>7. Cuánto tiempo los conservamos</h2>
<ul>
  <li>Solicitudes de invitación: hasta el final de la edición solicitada y como máximo 12 meses después, para poder tenerte en cuenta en la siguiente noche, o hasta que nos pidas suprimirlas.</li>
  <li>Noticias de próximas noches: hasta que te des de baja o retires tu consentimiento.</li>
</ul>
<p>Después, suprimimos los datos o los mantenemos bloqueados solo durante el plazo legal necesario para atender posibles reclamaciones.</p>

<h2>8. Tus derechos</h2>
<p>Puedes solicitar el acceso, la rectificación o la supresión de tus datos, oponerte a su tratamiento o pedir su limitación, recibirlos en un formato portable y retirar tu consentimiento en cualquier momento, sin que ello afecte a lo realizado antes. Escríbenos a <a href="mailto:{email}?subject=Privacidad">{email}</a> indicando “Privacidad” en el asunto. Si consideras que no hemos tratado tus datos correctamente, puedes reclamar ante la Agencia Española de Protección de Datos (AEPD), <a href="https://www.aepd.es" target="_blank" rel="noopener">www.aepd.es</a>.</p>

<h2>9. Edad</h2>
<p>ZAYA es para adultos. Debes tener 18 años o más para solicitar una invitación. Si sabemos que una solicitud procede de un menor de 18 años, la eliminamos.</p>

<h2>10. Seguridad y cambios</h2>
<p>Aplicamos medidas técnicas y organizativas razonables para proteger tus datos. Si esta política cambia, publicaremos aquí la nueva versión con su fecha.</p>
""",
}

PAGES["cookies"] = {
    "title": "Cookies — ZAYA",
    "desc": "zayaritual.com does not use cookies. How we count visits without them.",
    "h_en": "Cookies", "h_es": "Cookies",
    "en": """
<p class="lede">This website does not use cookies. That is why you never see a cookie banner here.</p>
<h2>No cookies, no tracking</h2>
<p>We do not use advertising cookies, tracking pixels, social media plugins or any third-party cookies, and we do not store anything on your device.</p>
<h2>How we count visits</h2>
<p>We use Vercel Web Analytics, which works without cookies. It records anonymous, aggregated information — the page visited, the referring site, country, device type and browser — and recognises a returning visit only through a temporary anonymous code that is discarded after 24 hours. It cannot identify you.</p>
<h2>What loads from where</h2>
<p>The fonts, images, films and music on this site are all served from zayaritual.com itself. Other services are contacted only when you act: Instagram when you follow a link to it, and our form provider when you send an invitation request (see the <a href="/privacy">privacy policy</a>).</p>
<h2>If this changes</h2>
<p>If we ever use cookies that need your consent, we will ask for it first and update this page.</p>
""",
    "es": """
<p class="lede">Este sitio web no utiliza cookies. Por eso nunca verás aquí un aviso de cookies.</p>
<h2>Sin cookies, sin rastreo</h2>
<p>No usamos cookies publicitarias, píxeles de seguimiento, complementos de redes sociales ni cookies de terceros, y no guardamos nada en tu dispositivo.</p>
<h2>Cómo contamos las visitas</h2>
<p>Usamos Vercel Web Analytics, que funciona sin cookies. Registra información anónima y agregada (la página visitada, el sitio de procedencia, el país, el tipo de dispositivo y el navegador) y solo reconoce una visita repetida mediante un código anónimo temporal que se elimina a las 24 horas. No puede identificarte.</p>
<h2>Qué se carga y desde dónde</h2>
<p>Las fuentes, imágenes, vídeos y música de este sitio se sirven desde el propio zayaritual.com. Solo se contacta con otros servicios cuando tú actúas: Instagram si sigues un enlace, y nuestro proveedor de formularios cuando envías una solicitud de invitación (ver la <a href="/privacy#es">política de privacidad</a>).</p>
<h2>Si esto cambia</h2>
<p>Si alguna vez usamos cookies que requieran tu consentimiento, te lo pediremos antes y actualizaremos esta página.</p>
""",
}
