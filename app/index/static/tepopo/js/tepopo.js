function input_to_tepopo(payafa, tepopopa, tepopoka, repepeka,
  rehepeka, belenepa, beleneka, kele_rehepe, tape_tepopo,
  fuku_tepopo, tere_tepopo, bulu_tepopo) {
    //console.log("convert common input text to tepopo");
    //console.log("input_to_tepepo()");
    let tepopo = tepopopa.querySelector("."+tepopoka)
    tepopo.addEventListener("focus", () => {
      fuku_tepopo(payafa,repepeka,rehepeka,kele_rehepe,
        tepopopa,tepopoka,belenepa,beleneka); });
    tepopo.addEventListener("blur", () => {
      bulu_tepopo(tepopopa,repepeka); });
    tepopo.addEventListener("keyup", (event) => {
        if(event.currentTarget.value !== "") {
            if(event.key == "Enter") {
                tepopo.blur();
                tere_tepopo(payafa,tepopopa,tepopoka,
                  belenepa,beleneka);
            } else {
                tape_tepopo(payafa,repepeka,rehepeka,
                  kele_rehepe,tepopopa,tepopoka,belenepa,
                  beleneka);
            }
        } else {
            let repepe = tepopopa.querySelector("."+repepeka);
            if(repepe !== null) {
                repepe.remove();
            }
        }
    });
}
//
async function folo_belene(payafa,belenepa,beleneka,tepopova) {
    //console.log("user want to fill the belene");
    //console.log("folo_belene()");
    //
    let belenele = await gete_resope(payafa,tepopova);
    //
    let belene = belenepa.querySelector("."+beleneka);
    belene.innerHTML = "";
    //
    hede = document.createElement('div');
    hede.classList.add("td");
    //
    for(let bele of belenele) {
        //
        let hebe = null;
        let hehe = null;
        let heha = null;
        //
        hebe = document.createElement('div');
        hebe.classList.add("tr");
        //
        /*
        <div class="tr">
          <div class="td">
            <a class="td" href="/order/banorene" title="заявка" target="_blank" data-hale="banorene">banorene</a>
          </div>
          <div class="td">
            <a class="td" href="https://www.galakmet.ru/" title="персона" target="_blank" data-hale="galagala">ООО "Галактика"</a>
          </div>
          <div class="td">
            <a class="td" href="/curcy/yolugebu" title="заберу" target="_blank" data-hale="yolugebu">м труба АД31.Т1.КР 18x2,0x6000 ГОСТ-18475-82</a>
          </div>
          <div class="td">
            <a class="td" href="/curcy/tulutulu" title="отдам" target="_blank" data-hale="tulutulu">руб </a>
          </div>
          <div class="td">
            <a class="td" href="#" title="отколичество" target="_self">
              118
            </a>
          </div>
        </div>
        */
        //
        hehe = document.createElement('div');
        hehe.classList.add("td");
        //
        heha = document.createElement('a');
        heha.classList.add("td");
        heha.innerHTML = bele.zovohale_hale;
        //
        hehe.append(heha);
        hebe.append(hehe);
        //
        //
        hehe = document.createElement('div');
        hehe.classList.add("td");
        //
        heha = document.createElement('a');
        heha.classList.add("td");
        heha.innerHTML = bele.perehale_name;
        //
        hehe.append(heha);
        hebe.append(hehe);
        //
        //
        hehe = document.createElement('div');
        hehe.classList.add("td");
        //
        heha = document.createElement('a');
        heha.classList.add("td");
        heha.innerHTML = bele.tevehalebe_name;
        //
        hehe.append(heha);
        hebe.append(hehe);
        //
        //
        hehe = document.createElement('div');
        hehe.classList.add("td");
        //
        heha = document.createElement('a');
        heha.classList.add("td");
        heha.innerHTML = bele.zovokalebe;
        //
        hehe.append(heha);
        hebe.append(hehe);
        //
        //
        hehe = document.createElement('div');
        hehe.classList.add("td");
        //
        heha = document.createElement('a');
        heha.classList.add("td");
        heha.innerHTML = bele.tevehalepe_name;
        //
        hehe.append(heha);
        hebe.append(hehe);
        //
        //
        hehe = document.createElement('div');
        hehe.classList.add("td");
        //
        heha = document.createElement('a');
        heha.classList.add("td");
        heha.innerHTML = bele.zovokalepe;
        //
        hehe.append(heha);
        hebe.append(hehe);
        //
        //
        hede.append(hebe);
    }
    belene.append(hede);
}
//
function kele_rehepe(event,payafa,tepopopa,tepopoka,
  belenepa,beleneka) {
    //console.log("user click on rehepe");
    //console.log("kele_rehepe()");
    let rehepe = event.currentTarget;
    let rehepeva = rehepe.innerHTML;
    let tepopo = tepopopa.querySelector("."+tepopoka);
    tepopo.value = rehepeva;
    //
    let tepopova = rehepeva;
    //
    tepopo.blur();
    //send tepopova to server
    folo_belene(payafa,belenepa,beleneka,tepopova);
}
//
async function gete_resope(payafa,tepopova) {
    //console.log("user want to get resope");
    //console.log("gete_resope()");
    //
    let hobode = {
        "command":"search",
        "text":tepopova,
    }
    let resope = await hobode_to_resope(hobode,payafa);
    //
    return(resope);
}
//
function resope_to_rehepele(resope) {
    //console.log("convert resope to rehepele");
    //console.log("resope_to_rehepele()");
    let rehepele = [];
    for(let resopehe of resope) {
        let resopeve = []
        for(let ke in resopehe) {
            resopeve.push(resopehe[ke]);
            break;
        }
        let resopevesa = resopeve.join("");
        rehepele.push(resopevesa);
    }
    return(rehepele);
}
//
async function gete_rehepele(payafa,tepopova) {
    //console.log("get rehepele from db");
    //console.log("gete_rehepele()");
    //
    let resope = await gete_resope(payafa,tepopova);
    //
    let rehepele = resope_to_rehepele(resope);
    //
    return(rehepele);
}
//
async function tape_tepopo(payafa,repepeka,rehepeka,
  kele_rehepe,tepopopa,tepopoka,belenepa,beleneka) {
    //console.log("user type on tepopo");
    //console.log("tape_tepopo()");
    //
    let tepopo = tepopopa.querySelector("."+tepopoka);
    let tepopova = tepopo.value;
    let rehepele = await gete_rehepele(payafa,tepopova);
    //
    let hepeve = tepopo.clientWidth;
    let hepeha = tepopo.clientHeight;
    let hepeto = tepopo.offsetTop + tepopo.clientHeight;
    //
    let hepe = document.createElement('div');
    hepe.classList.add(repepeka);
    hepe.style.width = hepeve + "px";
    hepe.style.maxHeight = hepeha*4 + "px";
    hepe.style.top = hepeto + "px";
    //
    for(let rehepe of rehepele) {
        let hehe = document.createElement('div');
        hehe.classList.add(rehepeka);
        hehe.style.height = hepeha + "px";
        //hehe.style.width = hepeve;
        hehe.addEventListener("click", (event) => {
          kele_rehepe(event,payafa,tepopopa,tepopoka,
            belenepa,beleneka); });
        hehe.innerHTML = rehepe;
        hepe.append(hehe);
    }
    //
    let repepe = tepopopa.querySelector("."+repepeka);
    if(repepe !== null) {
        repepe.remove();
    }
    tepopopa.append(hepe);
}
//
function fuku_tepopo(payafa,repepeka,rehepeka,kele_rehepe,
  tepopopa,tepopoka,belenepa,beleneka) {
    //console.log("user focus on tepopo");
    //console.log("fuku_tepopo()");
    //
    let tepopo = tepopopa.querySelector("."+tepopoka);
    if(tepopo.value !== "") {
        tape_tepopo(payafa,repepeka,rehepeka,kele_rehepe,
          tepopopa,tepopoka,belenepa,beleneka);
    } else {
        console.log();
    }
    //
}
//
function tere_tepopo(payafa,tepopopa,tepopoka,belenepa,
  beleneka) {
    //console.log("user press enter on tepopo");
    //console.log("tere_tepopo()");
    //
    let tepopo = tepopopa.querySelector("."+tepopoka);
    let tepopova = tepopo.value;
    //
    folo_belene(payafa,belenepa,beleneka,tepopova);
}
//
async function bulu_tepopo(tepopopa,repepeka) {
    //console.log("user blur on tepopo");
    //console.log("bulu_tepopo()");
    //
    await new Promise(r => setTimeout(r, 100));
    //
    let repepe = tepopopa.querySelector("."+repepeka);
    if(repepe !== null) {
        repepe.remove();
    }
    //
}
//
async function hobode_to_resope(hobode,sereve) {
  //console.log("convert hobode to resope");
  //console.log("hobode_to_resope()");
  //
  let rekuhe = await fetch(sereve, {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8"
    },
    body: JSON.stringify(hobode)
  });
  let resule = await rekuhe.text();
  let resulede = JSON.parse(resule);
  return(resulede);
}
function input_to_tepopo_short(payafa,tepopopa,belenepa) {
    input_to_tepopo(payafa,tepopopa,"tepopo","repepe",
        "rehepe",belenepa,"belene",
        kele_rehepe,tape_tepopo,fuku_tepopo,
        tere_tepopo,bulu_tepopo);
}
//
//let tepopopa = document.querySelector(".tepopopa");
//let belenepa = document.querySelector(".belenepa");
//let payafa = "kulebe.py";
//input_to_tepopo_short(payafa,tepopopa,belenepa)
//
