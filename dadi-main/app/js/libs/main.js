"use strict";document.addEventListener("DOMContentLoaded",()=>{gsap.registerPlugin(ScrollTrigger);const r=new LazyLoad({use_native:!0}),a=new LazyLoad({});function s(e,t,r){e=e.querySelector(t);e&&e.classList.remove(r)}var e=document.querySelectorAll(".p-lang"),e=(e[0]&&e.forEach(e=>{e.querySelector(".p-lang__current").addEventListener("click",()=>{e.classList.toggle("active")})}),document.querySelectorAll(".p-select")),e=(e[0]&&e.forEach(l=>{var e=l.querySelector(".p-select__current");const r=e.querySelector(".p-select__current-item"),t=l.querySelector(".p-select__abs"),a=e.querySelector("input");var o=t.querySelectorAll(".p-select__abs-item");e.addEventListener("click",()=>{l.classList.toggle("active")}),o.forEach(e=>{e.addEventListener("click",()=>{s(t,".p-select__abs-item.active","active"),a.value=e.dataset.value,r.textContent=e.dataset.value,l.classList.remove("active"),e.classList.add("active")})});const c=l.querySelectorAll(".p-checkboxes .p-checkboxes__item");if(c[0]){let a=[];c.forEach((e,t)=>{e.querySelector("input").checked&&a.push(t)}),c.forEach((e,t)=>{e.addEventListener("change",()=>{e.querySelector("input").checked?a.push(t):a=a.filter(e=>e!==t),r.textContent=function(){let r="";return a.forEach((e,t)=>{a.length!==t+1?r+=c[e].querySelector(".p-checkboxes__item-title").textContent+", ":r+=c[e].querySelector(".p-checkboxes__item-title").textContent}),r=a.length?r:l.dataset.textDefault}()})})}}),document.querySelectorAll(".why")),e=(e[0]&&e.forEach(r=>{var e=r.querySelectorAll(".why__tabs .why__tab");const a=r.querySelectorAll(".why__contents .why__content"),l=r.querySelectorAll(".why__blocks .why__block");e.forEach((e,t)=>{e.addEventListener("click",()=>{s(r,".why__tabs .why__tab.active","active"),s(r,".why__contents .why__content.active","active"),s(r,".why__blocks .why__block.active","active"),e.classList.add("active"),a[t].classList.add("active"),l[t].classList.add("active")})}),a.forEach(l=>{var e=l.querySelectorAll(".why__content-tabs .why__content-tab");const o=l.querySelectorAll(".why__content-image img");e.forEach((r,a)=>{var e;r.classList.contains("active")&&((e=r.querySelector(".why__content-text")).style.height=e.scrollHeight+"px"),r.addEventListener("click",()=>{var e=".why__content-tabs .why__content-tab.active",t=l.querySelector(e+" .why__content-text"),t=(t&&(t.style.height=""),s(l,e,"active"),s(l,".why__content-image img.active","active"),r.classList.add("active"),r.querySelector(".why__content-text"));t.style.height=t.scrollHeight+"px",o[a].classList.add("active")})})}),l.forEach(l=>{l.querySelectorAll(".why__block-item").forEach(r=>{const a=r.querySelector(".why__content-tab");var e;a&&a.classList.contains("active")&&((e=a.querySelector(".why__content-text")).style.height=e.scrollHeight+"px"),a&&a.addEventListener("click",()=>{var e=".why__block-item .why__content-tab.active",t=l.querySelector(e+" .why__content-text"),t=(t&&(t.style.height=""),s(l,e,"active"),s(l,".why__block-item.active","active"),a.classList.add("active"),a.querySelector(".why__content-text"));t.style.height=t.scrollHeight+"px",r.classList.add("active")})})})}),document.querySelectorAll(".estate__swiper")),e=(e[0]&&e.forEach(e=>{var t=e.querySelector(".swiper");t.classList.contains(".p-card__swiper")||new Swiper(t,{slidesPerView:"auto",navigation:{nextEl:e.querySelector(".swiper-button-next"),prevEl:e.querySelector(".swiper-button-prev")},mousewheel:{forceToAxis:!0},breakpoints:{320:{spaceBetween:10},769:{spaceBetween:18}}})}),document.querySelectorAll(".estate")),e=(e[0]&&e.forEach(r=>{var e=r.querySelectorAll(".estate_fav__tabs .estate_fav__tab");if(e[0]){const a=r.querySelectorAll(".estate_fav__items .estate_fav__item");e.forEach((e,t)=>{e.addEventListener("click",()=>{s(r,".estate_fav__tabs .estate_fav__tab.active","active"),s(r,".estate_fav__items .estate_fav__item.active","active"),e.classList.add("active"),a[t].classList.add("active")})})}}),document.querySelectorAll(".buy")),e=(e[0]&&e.forEach(t=>{var r=t.querySelector(".buy__row");const e=r.offsetWidth;e,window.innerWidth;t=gsap.utils.toArray(t.querySelectorAll(".buy__item"));if(1160<=window.innerWidth)gsap.to(t,{x:-e,ease:"none",scrollTrigger:{trigger:r,start:"center center",pin:!0,scrub:1,end:()=>"+="+e,invalidateOnRefresh:!0}});else{let e=t[0].scrollWidth*(t.length-1);gsap.to(t,{x:-e,ease:"none",scrollTrigger:{trigger:r,start:"center center",pin:!0,scrub:1,end:()=>"+="+e,invalidateOnRefresh:!0}})}}),document.querySelectorAll(".filters")),e=(e[0]&&e.forEach(e=>{const t=e.querySelector(".filters__coub"),r=e.querySelector(".filters__map"),a=e.querySelector(".filters__content"),l=e.querySelector(".filters__content-map");t.addEventListener("click",()=>{t.classList.add("active"),a.classList.add("active"),l.classList.remove("active"),r.classList.remove("active"),ScrollTrigger.refresh()}),r.addEventListener("click",()=>{t.classList.remove("active"),a.classList.remove("active"),l.classList.add("active"),r.classList.add("active"),ScrollTrigger.refresh()})}),document.querySelectorAll(".reviews__swiper")),e=(e[0]&&e.forEach(e=>{new Swiper(e.querySelector(".swiper"),{slidesPerView:3,spaceBetween:40,pagination:{clickable:!0,el:e.querySelector(".swiper-pagination")},mousewheel:{forceToAxis:!0}})}),document.querySelectorAll(".article-items")),e=(e[0]&&e.forEach(e=>{new Swiper(e.querySelector(".swiper"),{slidesPerView:"auto",spaceBetween:41,mousewheel:{forceToAxis:!0}})}),document.querySelectorAll(".best__swiper")),e=(e[0]&&e.forEach(e=>{new Swiper(e.querySelector(".swiper"),{slidesPerView:"auto",navigation:{nextEl:e.querySelector(".swiper-button-next"),prevEl:e.querySelector(".swiper-button-prev")},mousewheel:{forceToAxis:!0},breakpoints:{320:{spaceBetween:47},768:{spaceBetween:61}}})}),document.querySelectorAll(".p-card_filter")),e=(e[0]&&e.forEach(e=>{var t=e.querySelector(".swiper");new Swiper(t,{slidesPerView:"auto",pagination:{clickable:!0,el:e.querySelector(".swiper-pagination")},mousewheel:{forceToAxis:!0}})}),document.querySelectorAll(".p-card_second"));e[0]&&e.forEach(e=>{var t=e.querySelector(".p-card__swiper");new Swiper(t,{slidesPerView:"auto",allowTouchMove:!1,pagination:{clickable:!0,el:e.querySelector(".p-card__swiper-pagination")},mousewheel:{forceToAxis:!0}})});const d={firstDayOfWeek:1,weekdays:{shorthand:["Вс","Пн","Вт","Ср","Чт","Пт","Сб"],longhand:["Воскресенье","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]},months:{shorthand:["Янв","Фев","Март","Апр","Май","Июнь","Июль","Авг","Сен","Окт","Ноя","Дек"],longhand:["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]}};var e=document.querySelectorAll(".rent-single"),e=(e[0]&&e.forEach(t=>{const l=t.querySelector(".rent-single__right-date_start");if(l){const c=t.querySelector(".rent-single__right-date_end"),n=t.querySelector(".rent-single__col-date_start"),i=t.querySelector(".rent-single__col-date_end");var r=t.querySelector(".rent-single__right-input input");flatpickr(r,{minDate:"today",mode:"range",inline:!0,dateFormat:"d.m.Y",locale:d,onChange:function(e,t,r){var a={year:"numeric",month:"long",day:"numeric"};e[0]&&(l.textContent=e[0].toLocaleDateString("ru",a),n.textContent=e[0].toLocaleDateString("ru")),e[1]?(c.textContent=e[1].toLocaleDateString("ru",a),i.textContent=e[1].toLocaleDateString("ru")):(c.textContent=e[0].toLocaleDateString("ru",a),i.textContent=e[0].toLocaleDateString("ru"))}})}var r=t.querySelectorAll(".rent-single__select"),r=(r[0]&&r.forEach(t=>{t.querySelector(".rent-single__select-current").addEventListener("click",e=>{u(e),t.classList.toggle("active")}),t.querySelector(".rent-single__select-close").addEventListener("click",e=>{u(e),t.classList.remove("active")})}),t.querySelectorAll(".rent-single__quantity")),r=(r[0]&&r.forEach(e=>{var t=e.querySelector(".rent-single__quantity-minus"),r=e.querySelector(".rent-single__quantity-plus");const a=e.querySelector(".rent-single__quantity-input input"),l=e.closest(".rent-single__select").querySelector(".rent-single__select-title"),o=JSON.parse(e.dataset.texts);function c(e){var t;l.textContent=e+" "+(e=e,(t=(t=o)||["товар","товара","товаров"])&&t[4<e%100&&e%100<20?2:[2,0,1,1,1,2][e%10<5?e%10:5]])}t.addEventListener("click",e=>{u(e);e=parseInt(a.value);e<=1?a.value=1:(e--,a.value=e),c(a.value)}),r.addEventListener("click",e=>{u(e);e=parseInt(a.value);e++,a.value=e,c(a.value)})}),t.querySelectorAll(".rent-single__list")),r=(r[0]&&r.forEach(t=>{const r=t.dataset.count,a=t.querySelectorAll(".rent-single__list-li"),l=t.querySelector(".rent-single__list-li_more");l.addEventListener("click",()=>{var e=t.dataset.status;a.forEach((e,t)=>{r<=t&&e.classList.toggle("active")}),"true"===e&&(t.dataset.status="false",l.textContent=l.dataset.textHide),"false"===e&&(t.dataset.status="true",l.textContent=l.dataset.textShow)})}),t.querySelectorAll(".rent-single__rules")),r=(r[0]&&r.forEach(r=>{var e=r.querySelectorAll(".rent-single__rules-tab");const a=r.querySelectorAll(".rent-single__rules-content");e.forEach((e,t)=>{e.addEventListener("click",()=>{s(r,".rent-single__rules-tab.active","active"),s(r,".rent-single__rules-content.active","active"),e.classList.add("active"),a[t].classList.add("active")})})}),t.querySelector(".rent-single__floor")),a=(r&&(a=r.querySelector(".swiper"),new Swiper(a,{slidesPerView:"auto",spaceBetween:18,navigation:{nextEl:r.querySelector(".swiper-button-next"),prevEl:r.querySelector(".swiper-button-prev")},mousewheel:{forceToAxis:!0}})),t.querySelector(".rent-single__subitem"));if(a){var r=a.closest(".rent-single__row"),o=t.querySelector(".rent-single__right-item");let e=r.offsetHeight-a.offsetHeight-parseInt(window.getComputedStyle(a).top);o&&(e=e-o.offsetHeight-parseInt(window.getComputedStyle(o).marginBottom)),ScrollTrigger.create({trigger:a,start:"top top",end:`+=${e}px`,pin:!0})}r=t.querySelectorAll(".rent-single__tabs");r[0]&&r.forEach(a=>{var e=a.querySelectorAll(".rent-single__tab-tops_price .rent-single__tab-top"),t=a.querySelectorAll(".rent-single__tab-tops_second .rent-single__tab-top");const l=a.querySelectorAll(".rent-single__day");e.forEach((e,t)=>{e.addEventListener("click",()=>{s(a,".rent-single__tab-tops_price .rent-single__tab-top.active","active"),s(a,".rent-single__day.active","active"),e.classList.add("active"),l[t].classList.add("active")})}),t[0]&&t.forEach((e,r)=>{e.addEventListener("click",()=>{s(a,".rent-single__tab-tops_second .rent-single__tab-top.active","active"),e.classList.add("active"),l.forEach(e=>{var t=e.querySelectorAll(".rent-single__day-seconds .rent-single__day-second");s(e,".rent-single__day-second.active","active"),t[r].classList.add("active")})})})})}),document.querySelectorAll(".rent")),e=(e[0]&&e.forEach(e=>{e.querySelectorAll(".rent__input_date").forEach(e=>{var t=e.querySelector("input");if(t){const r=flatpickr(t,{minDate:"today",dateFormat:"d.m.Y",locale:d,onChange:function(e,t,r){r=r.element;"start"===r.getAttribute("name")&&r.closest(".rent__form").querySelector('input[name="end"]')._flatpickr.set("minDate",t)}});e.querySelector(".rent__input-svg").addEventListener("click",()=>{r.toggle()})}})}),document.querySelectorAll(".modal_form")),e=(e[0]&&e.forEach(r=>{const a=r.querySelectorAll(".modal_register__changes .modal_register__change"),l=r.querySelectorAll(".modal_register__inputs .modal_register__inputs-item"),t=(a.forEach((e,t)=>{e.addEventListener("click",()=>{s(r,".modal_register__changes .modal_register__change.active","active"),s(r,".modal_register__inputs .modal_register__inputs-item.active","active"),(0===t?(a[1].classList.add("active"),l[1]):(a[0].classList.add("active"),l[0])).classList.add("active")})}),r.querySelectorAll(".modal_conf__items .modal_conf__item")),o=r.querySelector(".modal_conf__end-link");t[0]&&o.addEventListener("click",()=>{var e=o.dataset.index;s(r,".modal_conf__items .modal_conf__item.active","active"),"2"===e?(t[0].classList.add("active"),o.dataset.index=1):(t[1].classList.add("active"),o.dataset.index=2)})}),document.querySelector(".cabinet")),e=(e&&((t=e.querySelectorAll(".cabinet__change-label_date"))[0]&&t.forEach(e=>{e=e.querySelector("input");flatpickr(e,{dateFormat:"d.m.Y",locale:d})}),e.querySelector(".cabinet__card"))&&(t=e.querySelector('.cabinet__card-second input[name="term"]'),flatpickr(t,{dateFormat:"m/y",locale:d})),document.querySelectorAll(".modal_filter__range")),t=(e[0]&&e.forEach(e=>{var t,r,a,l=e.querySelector(".modal_filter__range-main"),o=parseFloat(e.dataset.min),c=parseFloat(e.dataset.max);let n=e.dataset.string;n?(n=JSON.parse(n),r=e.dataset.start,t=e.dataset.end,noUiSlider.create(l,{start:[r,t],range:{min:0,max:n.length-1},step:1,tooltips:!0,format:{to:function(e){return n[Math.round(e)]},from:function(e){return n.indexOf(e)}}})):(r=e.dataset.type,a=[e.querySelector('input[name*="min"]'),e.querySelector('input[name*="max"]')],r&&"int"===r?noUiSlider.create(l,{start:[o,c],step:1,range:{min:o,max:c},tooltips:{to:function(e){return e.toFixed(0)}}}):noUiSlider.create(l,{start:[o,c],range:{min:o,max:c},tooltips:!0}),l.noUiSlider.on("update",function(e,t){a[t].value=e[t]}))}),document.querySelectorAll(".modal_filter__item_change")),e=(t[0]&&t.forEach(r=>{var e=r.querySelectorAll(".p-checkboxes__item");const a=r.querySelectorAll(".modal_filter__range-content");e[0]&&e.forEach((e,t)=>{e.addEventListener("click",()=>{s(r,".modal_filter__range-content.active","active"),a[t].classList.add("active")})})}),document.querySelectorAll(".modal_filter__price-item_area")),t=(e[0]&&e.forEach(r=>{var e=r.querySelectorAll(".p-checkboxes__item");const a=r.querySelectorAll(".modal_filter__area-item");e[0]&&e.forEach((e,t)=>{e.addEventListener("click",()=>{s(r,".modal_filter__area-item.active","active"),a[t].classList.add("active")})})}),document.querySelector(".modal_filter")),e=(t&&t.closest("form").querySelector(".modal_filter__reset").addEventListener("click",()=>{var e=window.location;window.location.href=e.protocol+"//"+e.host+e.pathname}),document.querySelectorAll(".team")),t=(e[0]&&e.forEach(e=>{var r=e.querySelector(".team__text-items");let a=e.querySelector(".team__text-line .team__text-line-circle");var l=r.querySelectorAll(".team__text-item");if(1160<=window.innerWidth){let t=gsap.timeline({scrollTrigger:{trigger:e,start:"center center",pin:!0,scrub:1,end:"+=100%",ease:"power2",toggleActions:"play none none reverse",onUpdate:e=>{gsap.to(a,{top:100*e.progress.toFixed(2)+"%"})}}});l.forEach(e=>{t.fromTo(e,{opacity:0},{opacity:1})})}else{let t=gsap.timeline({scrollTrigger:{trigger:r.closest(".team__right"),start:"center center",pin:!0,scrub:1,end:"+="+r.clientHeight+"px",ease:"power2",toggleActions:"play none none reverse",onUpdate:e=>{gsap.to(a,{top:100*e.progress.toFixed(2)+"%"})}}});l.forEach(e=>{t.fromTo(e,{opacity:0},{opacity:1})})}}),document.querySelectorAll(".advs"));function l(s,e){s=gsap.utils.toArray(s);let t=(e=e||{}).onChange,r=0,d=gsap.timeline({repeat:e.repeat,onUpdate:t&&function(){var e=d.closestIndex();r!==e&&(r=e,t(s[e],e))},paused:e.paused,defaults:{ease:"none"},onReverseComplete:()=>d.totalTime(d.rawTime()+100*d.duration())}),o=s.length,c=s[0].offsetLeft,u=[],n=[],i=[],_=[],l=0,p=!1,a=e.center,g=100*(e.speed||1),v=!1===e.snap?e=>e:gsap.utils.snap(e.snap||1),y=0,m=!0!==a&&gsap.utils.toArray(a)[0]||s[0].parentNode,h,f=()=>{let r=m.getBoundingClientRect(),a;s.forEach((e,t)=>{n[t]=parseFloat(gsap.getProperty(e,"width","px")),_[t]=v(parseFloat(gsap.getProperty(e,"x","px"))/n[t]*100+gsap.getProperty(e,"xPercent")),a=e.getBoundingClientRect(),i[t]=a.left-(t?r.right:r.left),r=a}),gsap.set(s,{xPercent:e=>_[e]}),h=s[o-1].offsetLeft+_[o-1]/100*n[o-1]-c+i[0]+s[o-1].offsetWidth*gsap.getProperty(s[o-1],"scaleX")+(parseFloat(e.paddingRight)||0)},S,q=()=>{y=a?d.duration()*(m.offsetWidth/2)/h:0,a&&u.forEach((e,t)=>{u[t]=S(d.labels["label"+t]+d.duration()*n[t]/2/h-y)})},w=(e,t,r)=>{let a=e.length,l=1e10,o=0,c;for(;a--;)(c=(c=Math.abs(e[a]-t))>r/2?r-c:c)<l&&(l=c,o=a);return o},E=()=>{let e,t,r,a,l;for(d.clear(),e=0;e<o;e++)t=s[e],r=_[e]/100*n[e],l=(a=t.offsetLeft+r-c+i[0])+n[e]*gsap.getProperty(t,"scaleX"),d.to(t,{xPercent:v((r-l)/n[e]*100),duration:l/g},0).fromTo(t,{xPercent:v((r-l+h)/n[e]*100)},{xPercent:_[e],duration:(r-l+h-r)/g,immediateRender:!1},l/g).add("label"+e,a/g),u[e]=a/g;S=gsap.utils.wrap(0,d.duration())},b=e=>{var t=d.progress();d.progress(0,!0),f(),e&&E(),q(),e&&d.draggable?d.time(u[l],!0):d.progress(t,!0)},L;function x(e,t){t=t||{},Math.abs(e-l)>o/2&&(e+=e>l?-o:o);let r=gsap.utils.wrap(0,o,e),a=u[r];return a>d.time()!=e>l&&e!==l&&(a+=d.duration()*(e>l?1:-1)),(a<0||a>d.duration())&&(t.modifiers={time:S}),l=r,t.overwrite=!0,gsap.killTweensOf(L),0===t.duration?d.time(S(a)):d.tweenTo(a,t)}if(gsap.set(s,{x:0}),f(),E(),q(),window.addEventListener("resize",()=>b(!0)),d.toIndex=(e,t)=>x(e,t),d.closestIndex=e=>{var t=w(u,d.time(),d.duration());return e&&(l=t,p=!1),t},d.current=()=>p?d.closestIndex(!0):l,d.next=e=>x(d.current()+1,e),d.previous=e=>x(d.current()-1,e),d.times=u,d.progress(1,!0).progress(0,!0),e.reversed&&(d.vars.onReverseComplete(),d.reverse()),e.draggable&&"function"==typeof Draggable){L=document.createElement("div");let e=gsap.utils.wrap(0,1),o,c,t,n,i,r,a=()=>d.progress(e(c+(t.startX-t.x)*o)),l=()=>d.closestIndex(!0);"undefined"==typeof InertiaPlugin&&console.warn("InertiaPlugin required for momentum-based scrolling and snapping. https://greensock.com/club"),t=Draggable.create(L,{trigger:s[0].parentNode,type:"x",onPressInit(){var e=this.x;gsap.killTweensOf(d),r=!d.paused(),d.pause(),c=d.progress(),b(),o=1/h,i=c/-o-e,gsap.set(L,{x:c/-o})},onDrag:a,onThrowUpdate:a,overshootTolerance:0,inertia:!0,snap(e){if(Math.abs(c/-o-this.x)<10)return n+i;let t=-(e*o)*d.duration(),r=S(t),a=u[w(u,r,d.duration())],l=a-r;return Math.abs(l)>d.duration()/2&&(l+=l<0?d.duration():-d.duration()),n=(t+l)/d.duration()/-o},onRelease(){l(),t.isThrowing&&(p=!0)},onThrowComplete:()=>{l(),r&&d.play()}})[0],d.draggable=t}return d.closestIndex(!0),r=l,t&&t(s[l],l),d}t[0]&&t.forEach(e=>{e=e.querySelector(".advs__items").querySelectorAll(".advs__item");let r=gsap.utils.toArray(e);r.forEach((e,t)=>{t!==r.length-1&&ScrollTrigger.create({trigger:e,start:()=>e.offsetHeight<window.innerHeight?"top top":"bottom bottom",end:"+="+e.offsetHeight,pin:!0,pinSpacing:!1})})});e=document.querySelectorAll(".appartments"),e[0]&&e.forEach(e=>{l(e.querySelectorAll(".appartments__item"),{repeat:-1,paused:!1,speed:1.5})}),t=document.querySelectorAll(".devs"),t[0]&&t.forEach(e=>{e.querySelectorAll(".devs__item").forEach(e=>{e.classList.contains("devs__item_reverse")?l(e.querySelectorAll("picture"),{repeat:-1,paused:!1,speed:1.2,reversed:!0}):l(e.querySelectorAll("picture"),{repeat:-1,paused:!1,speed:1.2})})}),e=document.querySelectorAll(".compar");function u(e){e.preventDefault(),e.stopPropagation()}function o(e){e.classList.remove("active")}e[0]&&e.forEach(e=>{e=e.querySelectorAll(".compar__item");e[0]&&e.forEach(e=>{e.querySelectorAll(".compar__subitem").forEach(e=>{new Swiper(e.querySelector(".swiper"),{slidesPerView:1,spaceBetween:40,pagination:{clickable:!0,el:e.querySelector(".swiper-pagination")},mousewheel:{forceToAxis:!0}})})})});new class{constructor(){this.allModals(),this.allModalShows()}allModals(){document.querySelectorAll(".modal").forEach(t=>{function r(){var e;o(t),document.body.style.overflow="",e=new CustomEvent("pModalClose",{detail:{modal:t}}),document.dispatchEvent(e)}var e=t.querySelector(".modal__close"),e=(e&&e.addEventListener("click",()=>{r()}),t.querySelector(".modal__back"));e&&e.addEventListener("click",()=>{r()}),t.addEventListener("click",e=>{e.target==t&&r()})})}allModalShows(){document.querySelectorAll(".modal__show").forEach(t=>{t.addEventListener("click",e=>{u(e);e=t.getAttribute("data-modal"),e=document.querySelector(".modal_"+e),e.classList.add("active"),document.body.style.overflow="hidden",e=new CustomEvent("pModalOpen",{detail:{modal:e,element:t}});document.dispatchEvent(e)})})}},document.addEventListener("pModalOpen",e=>{var e=e.detail,t=e.element,e=e.modal;r.update(),a.update(),e.classList.contains("modal_like_2")&&o(t.closest(".modal"))})});