let ancientNames = {
    4: "libertas",
    5: "siyalatas",
    8: "mammon",
    9: "mimzee",
    10: "pluto",
    11: "dogcog",
    12: "fortuna",
    13: "atman",
    14: "dora",
    15: "bhaal",
    16: "morgulis",
    17: "chronos",
    18: "bubos",
    19: "fragsworth",
    20: "vaagur",
    21: "kumawakamaru",
    22: "chawedo",
    23: "hecatoncheir",
    24: "berserker",
    25: "sniperino",
    26: "kleptos",
    27: "energon",
    28: "argaiv",
    29: "juggernaut",
    31: "revolc",
    32: "nogardnit"
}

function checkList(missing, underleveled, ancients, list, treshold) {
    for (let i = 0; i < list.length; i++) {
        let ancientNo = list[i];
        if (ancients[ancientNo] && ancients[ancientNo].level) {
            let ancientLevel = ancients[ancientNo].level;
            let lastE = ancientLevel.lastIndexOf("e");
            let logAncientLevel = lastE > 0
                ? parseFloat(ancientLevel.substr(lastE + 1)) + Math.log10(ancientLevel.substr(0, lastE))
                : Math.log10(ancientLevel)
            if (logAncientLevel < treshold) underleveled.push(ancientNo);
        } else {
            missing.push(ancientNo);
        }
    }
}

let ascensionList = [
    [3700, 202300],
    [3924, 214000],
    [4150, 225800],
    [4380, 233100],
    [4520, 237500],
    [4605, 245100],
    [4754, 249776],
    [4844, 258893],
    [5021, 264435],
    [5128, 274275],
    [5319, 280257],
    [5435, 283895],
    [5435, 292569],
    [5505, 297843],
    [5673, 301050],
    [5576, 303000],
    [5838, 311581],
    [5875, 316798],
    [6042, 319971],
    [6143, 321900],
    [6204, 331225],
    [6242, 336894],
    [6423, 336894],
    [6532, 340342],
    [6599, 342438],
    [6640, 352590],
    [6837, 358763],
    [6956, 362516],
    [7029, 364798],
    [7073, 375820],
    [7287, 382521],
    [7417, 386595],
    [7496, 389073],
    [7544, 390579],
    [7573, 401854],
    [7791, 408710],
    [7924, 412879],
    [8005, 415414],
    [8054, 416955],
    [8084, 429008],
    [8318, 436336],
    [8460, 440792],
    [8546, 443502],
    [8599, 445149],
    [8631, 457993],
    [8880, 465802],
    [9031, 470550],
    [9123, 473437],
    [9179, 475193],
    [9213, 476260],
    [9234, 489507],
    [9490, 497561],
    [9646, 502458],
    [9741, 505436],
    [9799, 556967],
    [10798, 618650],
    [11993, 672444],
    [13036, 722181],
    [14000, 788703],
    [15289, 829151],
    [16073, 853746],
    [16550, 888767],
    [17229, 910061],
    [17642, 944483],
    [18309, 965414],
    [18714, 1000000]
]

function rubiesToQA(startHS, targetZone) {
    if (startHS > 18714) return 0;
    let rubyTotal = 0;
    for (let i = 0; i < ascensionList.length; i++) {
        let a = ascensionList[i]
        if (a[0] >= startHS) {
            if (a[1] > targetZone) { break; }
            rubyTotal += 50;
        }
    }
    return rubyTotal;
}

function checkAncients() {
    let data = userData.data;
    let heroSoulsInput = userData.heroSoulsInput;
    let borbLimit = userData.borbLimit;
    
    let chor = data.outsiders.outsiders[2].level;
    let heroSoulsTotal = data.totalHeroSoulsFromAscensions;
    let lastE = heroSoulsTotal.lastIndexOf("e");
    let heroSouls = lastE > 0
        ? parseFloat(heroSoulsTotal.substr(lastE + 1)) + Math.log10(heroSoulsTotal.substr(0, lastE))
        : Math.log10(heroSoulsTotal);
    heroSouls += Math.log10(1 / 0.95) * chor;
    
    let results = "";
    
    let ancients = data.ancients.ancients;
    let missing = [];
    let underleveled = [];
    if (!userData.useOnAscend) {
        //check argaiv, bhaal, fragsworth, libertas, mammon, mimzee, pluto and siyalatas
        checkList(missing, underleveled, ancients, [28, 15, 19, 4, 8, 9, 10, 5], (heroSouls - 5) / 2);
        //check juggernaut and nogardnit
        checkList(missing, underleveled, ancients, [29, 32], (heroSouls - 5) / 2.5);
        //check morgulis
        checkList(missing, underleveled, ancients, [16], heroSouls - 5);
        if (missing.length > 0) {
            results += "<b>Missing:</b> ";
            for (let a = 0; a < missing.length; a++) {
                results += ancientNames[missing[a]] + ", ";
            }
            results = results.slice(0, -2);
            results += "<br>";
        }
        if (underleveled.length > 0) {
            results += "<b>Underleveled:</b> ";
            for (let a = 0; a < underleveled.length; a++) {
                results += ancientNames[underleveled[a]] + ", ";
            }
            results = results.slice(0, -2);
            results += "<br>";
        }
    }
    
    //check rubies
    let rubies = data.rubies;
    let logHeroSouls;
    if (heroSoulsInput.indexOf("e") > -1) {
        let mantissa = heroSoulsInput.substr(0, heroSoulsInput.indexOf("e"));
        let exponent = heroSoulsInput.substr(heroSoulsInput.lastIndexOf("e") + 1);
        mantissa = parseFloat(mantissa || 0);
        exponent = parseFloat(exponent || 0);
        if ((isNaN(mantissa)) || isNaN(exponent)) {
            alert("Calculation failed. logHeroSouls must be a positive number.");
            $("#hero_souls").val(150);
            return false;
        }
        logHeroSouls = exponent + Math.log10(mantissa);
        mantissa = Math.pow(10, logHeroSouls % 1).toFixed(3);
        exponent = Math.floor(logHeroSouls);
        $("#hero_souls").val(mantissa + "e" + exponent);
    } else {
        logHeroSouls = parseFloat(heroSoulsInput || 0);
        $("#hero_souls").val(logHeroSouls);
    }
    let rubiesNeeded = 0;
    if (borbLimit > 200000) {
        rubiesNeeded = rubiesToQA(logHeroSouls, borbLimit + 1);
    }
    
    if (borbLimit < 0) {
        let mpzStart = -borbLimit / 5000 + 2;
        results += "You have " + mpzStart + " monsters per zone, leading to a longer ascension.";
        results += "<br>"
    } else if (userData.highestZone > (borbLimit + 499)) {
        results += "You will have more than 2 monsters per zone starting from zone " + (borbLimit + 500).toLocaleString() + ", leading to a longer ascension."
        results += "<br>"
    }
    let altAction = false;
    if (rubiesNeeded > rubies) {
        results += "You are low on rubies! You need roughly <b>" + rubiesNeeded + " rubies</b> total for QAs up to zone " + Math.min(borbLimit + 500, 1e6).toLocaleString() +". Consider <b>";
        if (logHeroSouls > 5040 || logHeroSouls <= 2600) {
            results += "saving your rubies</b>.";
            altAction = "Save your rubies."
        } else {
            results += "using a single 24 hour Timelapse</b>.";
            altAction = "Use a single 24h Timelapse."
        }
    }
    if (results !== "") {
        $("#ancientCheckResults").html(results);
        $("#ancientCheckResults").parent().show();
        $('html, body').animate({
            scrollTop: ($('.warning').offset().top)
        },200);
    } else {
        $("#ancientCheckResults").parent().hide();
        $('html, body').animate({
            scrollTop: ($('#results').offset().top)
        },200);
    }
    return altAction;
}