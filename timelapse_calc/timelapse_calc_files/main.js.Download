// Polyfill for Internet Explorer
Math.log10 = function(x) {
    return Math.log(x) / Math.LN10;
}

var userData = {};

var settingsVisible = false;

function showAdvancedClick() {
    $("#advancedSettings").toggle(100, function(){
        $("#showAdvanced").html( (settingsVisible = !settingsVisible) ? "Hide Advanced Settings" : "Show Advanced Settings");
    });
}

function setDefaults() {
    $("#minZones").val(20000);
    $("#ascTime").val(0);
    $("#QAStrat").val("perRuby");
}


function defaultClick() {
    setDefaults();
    refresh();
}

function getInputs() {
    let heroSoulsInput = $("#hero_souls").val();
    let logHeroSouls;
    if (heroSoulsInput.indexOf("e") > -1) {
        let mantissa = heroSoulsInput.substr(0, heroSoulsInput.indexOf("e"));
        let exponent = heroSoulsInput.substr(heroSoulsInput.lastIndexOf("e") + 1);
        mantissa = parseFloat(mantissa || 0);
        exponent = parseFloat(exponent || 0);
        if ((isNaN(mantissa)) || isNaN(exponent)) {
            alert("Calculation failed. logHeroSouls must be a positive number.");
            $("#hero_souls").val(150);
            return [0, 0, 0];
        }
        logHeroSouls = exponent + Math.log10(mantissa);
        mantissa = Math.pow(10, logHeroSouls % 1).toFixed(3);
        exponent = Math.floor(logHeroSouls);
        $("#hero_souls").val(mantissa + "e" + exponent);
    } else {
        logHeroSouls = parseFloat(heroSoulsInput || 0);
        $("#hero_souls").val(logHeroSouls);
    }
    if (!(logHeroSouls >= 0)) {
        alert("Calculation failed. logHeroSouls must be a positive number.");
        $("#hero_souls").val(150);
        return [-1, 0, 0];
    }

    let xyliqilLevel = parseFloat($("#xyliqil_level").val() || 0);
    if (!(xyliqilLevel >= 0)) { xyliqilLevel = 0; }
    xyliqilLevel = Math.floor(xyliqilLevel);
    $("#xyliqil_level").val(xyliqilLevel.toString().replace(/\+/g,''));

    let chorLevel = parseFloat($("#chor_level").val() || 0);
    if (!(chorLevel >= 0)) { chorLevel = 0; }
    if (chorLevel > 150) { chorLevel = 150; }
    chorLevel = Math.floor(chorLevel);
    $("#chor_level").val(chorLevel.toString().replace(/\+/g,''));

    let autoClickers = parseFloat($("#autoclickers").val() || 0);
    if (!(autoClickers >= 0)) { autoClickers = 0; }
    autoClickers = Math.floor(autoClickers);
    $("#autoclickers").val(autoClickers.toString().replace(/\+/g,''));
    

    let minZones = parseInt($("#minZones").val() || 1);
    if (!(minZones >= 1)) { minZones = 1; }
    $("#minZones").val(minZones);
    
    let ascTime = parseFloat($("#ascTime").val() || 0);
    if (!(ascTime >= 0)) { ascTime = 0; }
    $("#ascTime").val(ascTime);

    let QAStrat = $("#QAStrat").val();
    return {
        logHeroSouls: logHeroSouls,
        xyliqilLevel: xyliqilLevel,
        chorLevel: chorLevel,
        autoClickers: autoClickers,
        minZones: minZones,
        ascTime: ascTime,
        QAStrat: QAStrat
    }
}

let e11Levels = {
    Rose1: 602000,
    Rose2: 1204000,
    Rose3: 1806000,
    Rose4: 2408000,
    Rose5: 3010000,
    Sophia1: 677250,
    Sophia2: 1279250,
    Sophia3: 1881250,
    Sophia4: 2483250,
    Sophia5: 3085250,
    Blanche1: 752500,
    Blanche2: 1354500,
    Blanche3: 1956500,
    Blanche4: 2558500,
    Blanche5: 3160500,
    Dorothy1: 827750,
    Dorothy2: 1429750,
    Dorothy3: 1956500,
    Dorothy4: 2633750,
    Dorothy5: 3235750
};
let e11Dps = {
    Rose: Math.log10(8.586) + 148592,
    Sophia: Math.log10(6.326) + 158831,
    Blanche: Math.log10(4.661) + 178104,
    Dorothy: Math.log10(3.434) + 199738
};
let e11Upgrade = 5798;
let e11CostScale = Math.log10(1.22);
let e11DpsScale = Math.log10(1000);
let costThousand = Math.log10(1.07) * 1000;
let dogcog = 10;
let heroCosts = {
    Samurai: -10000,
    Atlas: 55 + Math.log10(1.07) * 725 - dogcog,
    Terra: 70 + costThousand - dogcog,
    Phthalo: 85 + costThousand - dogcog,
    Orntchya: 100 + costThousand - dogcog,
    Lilin: 115 + costThousand - dogcog,
    Cadmia: 130 + costThousand - dogcog,
    Alabaster: 145 + costThousand - dogcog,
    Astrea: 160 + costThousand - dogcog,
    Chiron: 175 + costThousand - dogcog,
    Moloch: 190 + costThousand - dogcog,
    BomberMax: 205 + costThousand - dogcog,
    Gog: 220 + costThousand - dogcog,
    Wepwawet: 235 + costThousand - dogcog,
    BettyClicker: 235 + costThousand * 1.5 - dogcog,
    KingMidas: 235 + costThousand * 2 - dogcog,
    Wepwawet2: 235 + costThousand * 5 - dogcog,
    Tsuchi: 500 - dogcog,
    Skogur: 1000 - dogcog,
    Moeru: 2000 - dogcog,
    Zilar: 4000 - dogcog,
    Madzi: 8000 - dogcog,
    Xavira0: 14000 - dogcog,
    Xavira1: 18407.5667 - dogcog,
    Xavira2: 19435.9989 - dogcog,
    Xavira3: 21492.8633 - dogcog,
    Xavira4: 22521.2955 - dogcog,
    Xavira5: 23872.9493 - dogcog,
    Cadu0: 25500 - dogcog,
    Ceus1: 27204.2591 - dogcog,
    Cadu1: 28908.5182 - dogcog,
    Ceus2: 30789.08 - dogcog,
    Cadu2: 32845.9444 - dogcog,
    Ceus3: 35079.1115 - dogcog,
    Cadu3: 37473.8894 - dogcog,
    Ceus4: 40044.97 - dogcog,
    Cadu4: 42777.6613 - dogcog,
    Maw0: 45500 - dogcog,
    Maw1: 48761.5993 - dogcog,
    Maw2: 52184.8094 - dogcog,
    Maw3: 55784.3222 - dogcog,
    Maw4: 59545.4457 - dogcog,
    Maw5: 63497.5683 - dogcog,
    Maw6: 67611.2927 - dogcog,
    Yachiyl1: 76627.945 - dogcog,
    Yachiyl2: 81432.1926 - dogcog,
    Yachiyl3: 86398.0511 - dogcog,
    Yachiyl4: 91540.2122 - dogcog,
    Yachiyl5: 96858.6759 - dogcog,
    Yachiyl6: 102338.7505 - dogcog
};
let heroCosts1 = {
    Samurai: 5 - dogcog,
    Atlas: 55 - dogcog,
    Terra: 70 - dogcog,
    Phthalo: 85 - dogcog,
    Orntchya: 100 - dogcog,
    Lilin: 115 - dogcog,
    Cadmia: 130 - dogcog,
    Alabaster: 145 - dogcog,
    Astrea: 160 - dogcog,
    Chiron: 175 - dogcog,
    Moloch: 190 - dogcog,
    BomberMax: 205 - dogcog,
    Gog: 220 - dogcog,
    Wepwawet: 235 - dogcog,
    BettyClicker: Math.log10(20000) - dogcog,
    KingMidas: Math.log10(4e12) - dogcog,
    Tsuchi: 500 - dogcog,
    Skogur: 1000 - dogcog,
    Moeru: 2000 - dogcog,
    Zilar: 4000 - dogcog,
    Madzi: 8000 - dogcog,
    Xavira: 14000 - dogcog,
    Cadu: 25500 - dogcog,
    Ceus: 25500 - dogcog,
    Maw: 45500 - dogcog,
    Yachiyl: 72000 - dogcog,
    Rose: 108000 - dogcog,
    Sophia: 114500 - dogcog,
    Blanche: 127500 - dogcog,
    Dorothy: 142200 - dogcog
};
let heroBaseDps = {
    Samurai: 5.2858,
    Atlas: 47.4251,
    Terra: 60.2924,
    Phthalo: 73.1598,
    Orntchya: 86.0271,
    Lilin: 98.8944,
    Cadmia: 111.7618,
    Alabaster: 124.6290,
    Astrea: 137.4965,
    Chiron: 149.4965,
    Moloch: 163.2312,
    BomberMax: 175.9437,
    Gog: 188.9871,
    Wepwawet: 201.7295,
    BettyClicker: 11.0038,
    KingMidas: 18.7950,
    Wepwawet2: 201.7295,
    Tsuchi: 427.7216,
    Skogur: 848.7439,
    Moeru: 1681.6906,
    Zilar: 3336.7651,
    Madzi: 6634.3112,
    Xavira0: 11683.4585,
    Xavira1: 12306.4585,
    Xavira2: 12954.4585,
    Xavira3: 13627.4585,
    Xavira4: 14475.4585,
    Xavira5: 15348.4585,
    Cadu0: 26446.3258,
    Ceus1: 27444.1931,
    Cadu1: 28544.3258,
    Ceus2: 29742.1931,
    Cadu2: 31042.3258,
    Ceus3: 32440.1931,
    Cadu3: 33940.3258,
    Ceus4: 35538.1931,
    Cadu4: 37238.3258,
    Maw0: 61732.0604,
    Maw1: 63730.0604,
    Maw2: 65828.0604,
    Maw3: 68026.0604,
    Maw4: 70324.0604,
    Maw5: 72722.0604,
    Maw6: 75220.0604,
    Yachiyl1: 101491.9278,
    Yachiyl2: 104389.9278,
    Yachiyl3: 107387.9278,
    Yachiyl4: 110485.9278,
    Yachiyl5: 113683.9278,
    Yachiyl6: 116981.9278
};

// Populate e11 heroes
let newHeroes = ["Rose", "Sophia", "Blanche", "Dorothy"];
for (let l = 0; l < 6; l++) {
    for (let q = 0; q < 4; q++) {
        let hero = newHeroes[q];
        let heroCost = heroCosts1[hero];
        let heroDps = e11Dps[hero];
        let heroUpgrade = hero + l;
        let level = e11Levels[heroUpgrade] || 0;
        heroCosts[heroUpgrade] = heroCost + level * e11CostScale;
        heroBaseDps[heroUpgrade] = heroDps + e11Upgrade * l + 1.861426728;
    }
}
heroCosts["Rose0"] += Math.log10(1.22) * 9700;

function findBestHero(logGold) {
    let bestHero;
    let heroType = "old";
    for (let s in heroCosts) {
        if (heroCosts.hasOwnProperty(s)) {
            if (heroCosts[s] <= logGold) {
                bestHero = s;
                if (s === "Xavira0") { heroType = "e10"; }
                if (s === "Rose0") { heroType = "e11"; }
            }
        }
    }
    return [bestHero, heroType];
}

function findNextHero(currentHero) {
    if (currentHero === "Dorothy5") return false;
    let logGold = heroCosts[currentHero];
    let nextHero;
    let heroType = "old";
    for (let s in heroCosts) {
        if (heroCosts.hasOwnProperty(s)) {
            if (s === "Xavira0") { heroType = "e10"; }
            if (s === "Rose0") { heroType = "e11"; }
            if (heroCosts[s] > logGold) {
                if (s !== "Dorothy1" && s !== "Dorothy2" && s !== "dorothy4") {
                    nextHero = s;
                    break;
                }
            }
        }
    }
    return [nextHero, heroType];
}

function findHeroDps(bestHero, heroLevel, heroType, gilds) {
    let baseDps = heroBaseDps[bestHero] + Math.log10(heroLevel);
    let damageMultiplier;
    if (heroType === "e11") {
        damageMultiplier = 1000;
    } else if (heroType === "e10") {
        damageMultiplier = 4.5;
    } else {
        damageMultiplier = 4;
    }
    let dpsMultiplier25 = Math.log10(damageMultiplier) * Math.floor(Math.max(heroLevel - 175, 0) / 25);
    let dpsMultiplier1000 = (heroType === "e11")
        ? 0
        : Math.log10(10 / damageMultiplier) * Math.min(Math.floor(heroLevel / 1000), 8);
    let gildDps = Math.log10(gilds);
    return baseDps + dpsMultiplier25 + dpsMultiplier1000 + gildDps;
}

let cacheHp140 = Math.log10(1.55) * 139 + 1;
let hp141 = 1 + Math.log10(1.145) + cacheHp140;
let hp500 = 1 + Math.log10(1.55) * 139 + Math.log10(1.145) * 360;
let hp200k = Math.log10(1.24) + 25409;

function findHighestZone(totalDps) {
    if (totalDps === Infinity) return 2.147e9;
    if (totalDps < hp141) {
        return 130;
    } else if (totalDps <= hp500) {
        return 500;
    } else if (totalDps < hp200k) {
        let logHealth = hp500;
        this.zone = 199999;
        for (let z = 501; z < 200000; z++) {
            logHealth += Math.log10(1.145 + 0.001 * Math.floor((z - 1) / 500));
            if (logHealth >= totalDps) {
                this.zone = z;
                break;
            }
        }
    } else {
        this.zone = Math.min((totalDps - hp200k) / Math.log10(1.545) + 200000, 2.147e9);
    }
    let bossMultiplier = Math.floor(this.zone / 500) * 0.4 + 5;
    this.zone -= Math.log(bossMultiplier) / Math.log(1.545);
    return Math.floor(this.zone);
}

function findHighestIdleZone(logHeroSouls, heroDps, xyliqilLevel, autoClickers) {
    let ancientDps = logHeroSouls * 2.4 + Math.log10(1.5) * 2 * xyliqilLevel -1.4457374595558059145523937994475;
    let totalDps = heroDps + ancientDps;
    if (autoClickers <= 2e9) {
        totalDps += Math.log10(1.5) * autoClickers;
    }
    return findHighestZone(totalDps);
}

function findHighestActiveZone(logHeroSouls, heroDps) {
    let ancientDps = logHeroSouls * 2.9 -1.8159188043029278373206243377068;
    let totalDps = heroDps + ancientDps;
    return findHighestZone(totalDps);
}

function getMonsterGold(level, logHeroSouls) {
    let ancientGold = logHeroSouls * 1.5 -1.1105440342413657683046916147778;
    if (level < 140) {
        return Math.log10(1.6) * (level - 1) + ancientGold - Math.log10(15);
    } else {
        return Math.log10(1.15) * (level - 140) + Math.log10(1.6) * 139 + ancientGold - Math.log10(15);
    }
}

function getHeroLevel(logGold, bestHero, heroType) {
    let nameShort = bestHero.substring(0, bestHero.length - 1);
    let baseCost = heroCosts1[nameShort]
        ? heroCosts1[nameShort]
        : heroCosts1[bestHero];
    let costMultiplier = (heroType === "e11" ) ? 1.22 : 1.07;
    let heroLevel = Math.floor((logGold - baseCost) / Math.log10(costMultiplier));
    heroLevel = Math.max(1, heroLevel);
    return heroLevel;
}

function getZoneRequired(currentHero, useActive, logCps, logXylBonus) {
    let goldRequired = heroCosts[currentHero] - Math.log10(1.15 / 0.15)
        - (useActive ? logCps : logXylBonus)
        - (userData.logHeroSouls * 1.5 -1.1105440342413657683046916147778)
        - Math.log10(1.6 / 1.15) * 139;
    let zoneRequired = Math.floor(goldRequired / Math.log10(1.15));
    return zoneRequired;
}

function getNextTL(startingZone) {
    let zonesGained = userData.highestZone - startingZone;
    let duration;
    let rubyCost;
    if (zonesGained <= userData.minZones) {
        return [false, zonesGained];
    }
    let needed = Infinity;
    if (userData.endZone) {
        if (startingZone > userData.endZone) {
            return [false, zonesGained];
        } else {
            needed = userData.endZone - startingZone;
        }
    }
    if ((zonesGained >= 360000) && (userData.minZones <= 756000) && (needed >= 252000)) {
        duration = "168h";
        zonesGained = Math.min(756000, zonesGained);
        rubyCost = 50;
    } else if ((zonesGained >= 144000) && (userData.minZones <= 216000) && (needed >= 108000)) {
        duration = "48h";
        zonesGained = Math.min(216000, zonesGained);
        rubyCost = 30;
    } else if ((zonesGained >= 72000) && (userData.minZones <= 108000) && (needed >= 36000)) {
        duration = "24h";
        zonesGained = Math.min(108000, zonesGained);
        rubyCost = 20;
    } else if (userData.minZones <= 36000) {
        duration = "8h";
        zonesGained = Math.min(36000, zonesGained);
        rubyCost = 10;
    } else {
        return [false, zonesGained];
    }
    userData.highestZone = startingZone + zonesGained;

    return [duration, zonesGained, rubyCost];
}

function getSoftCap(options, startingZone, logCps, logXylBonus, gilds) {
    userData.timelapseZoneMax = startingZone;
    let activeAdvantage = userData.logHeroSouls * 0.5 + logCps -0.3701813447471219227682305382593 - Math.log10(1.5) * 3.3895 * userData.xyliqilLevel;
    if (userData.autoClickers <= 2e9) {
        activeAdvantage -= Math.log10(1.5) * userData.autoClickers;
    } else {
        if (!options.test)
            console.log("Too many ACs, Nogardnit's scaling is broken past 2e9 ACs.");
    }
    let useActive = activeAdvantage > 0;
    if (!useActive && !options.test) { console.log("Idle is better than active."); }
    
    let goldRequired = false;
    do {
        let logGold = getMonsterGold(startingZone, userData.logHeroSouls);
        logGold += Math.log10(1.15 / 0.15);
        logGold += useActive ? logCps : logXylBonus;
        let IEsucks = findBestHero(logGold);
        let bestHero = IEsucks[0];
        let heroType = IEsucks[1];
        let heroLevel = getHeroLevel(logGold, bestHero, heroType);
        let heroDps = findHeroDps(bestHero, heroLevel, heroType, gilds);
        let combo = Math.log10(Math.max((startingZone - userData.timelapseZoneMax) / 2.25, 1)) + logCps;
        combo = Math.min(combo, 307);
        userData.highestZone = useActive
            ? findHighestActiveZone(userData.logHeroSouls, heroDps + combo + logCps)
            : findHighestIdleZone(userData.logHeroSouls, heroDps, userData.xyliqilLevel, userData.autoClickers);
        userData.highestZone = userData.highestZone - userData.highestZone % 5 + 4;

        zonesGained = userData.highestZone - startingZone;
        if (zonesGained <= 10) {
            return [startingZone, bestHero, heroLevel];
        } else {
            startingZone = userData.highestZone;
        }
    } while (zonesGained > 10);
}

function formatTime(durationSeconds) {
    let hours = Math.floor(durationSeconds / 3600);
    let duration;
    if (hours < 72) {
        let minutes = Math.floor((durationSeconds - (hours * 3600)) / 60);
        let seconds = durationSeconds - hours * 3600 - minutes * 60;
        if (hours   < 10) { hours   = "0" + hours; }
        if (minutes < 10) { minutes = "0" + minutes; }
        if (seconds < 10) { seconds = "0" + seconds; }
        duration = hours + ":" + minutes + ":" + seconds;
    } else {
        let dl = durationSeconds;
        let years = Math.floor(dl / 31557600);
        dl -= years * 31557600;
        let days = Math.floor(dl / 86400);
        dl -= days * 86400;
        hours = dl / 3600;
        duration = (years > 0 ? years.toLocaleString() + "y " : "") + days + "d " + hours.toFixed(2) + "h";
    }
    return duration;
}

function refresh(options) {
    if (options === undefined || options === null) options = {};
    if (options.test) {
        userData = Object.assign({}, options);
    } else {
        console.clear();
        userData = getInputs();
    }

    if (userData.logHeroSouls < 0) { return false; }
    
    if (options.data) {
        userData.data = options.data;
        userData.heroSoulsInput = options.heroSoulsInput;
        userData.useOnAscend = options.useOnAscend;
        let kumaLevel = userData.data.ancients.ancients[21].level;
        let kumaEffect = 8 * (1 - Math.exp(-0.025 * kumaLevel));
        let borbLevel = userData.data.outsiders.outsiders[6].level;
        let mpzReduction = kumaEffect * (1 + borbLevel / 8);
        userData.borbLimit = Math.floor((mpzReduction - 8) * 10) * 500;
    }
    
    if (!options.test) console.log(userData);
    
    
    let logCps = Math.max(1 + Math.log10(userData.autoClickers), 1 + (userData.autoClickers - 1) * Math.log10(1.5));
    if (logCps >= 307) {
        logCps = 2;
        if (!options.test)
            console.log("Too many ACs, assign a few on the monster only or progress will be broken.");
    }
    let logXylBonus = Math.log10(1.5) * userData.xyliqilLevel;
    
    let activeAdvantage = userData.logHeroSouls * 0.5 + logCps -0.3701813447471219227682305382593 - Math.log10(1.5) * 3.3895 * userData.xyliqilLevel;
    if (userData.autoClickers <= 2e9) {
        activeAdvantage -= Math.log10(1.5) * userData.autoClickers;
    } else {
        if (!options.test)
            console.log("Too many ACs, Nogardnit's scaling is broken past 2e9 ACs.");
    }
    let useActive = activeAdvantage > 0;
    if (!useActive && !options.test) { console.log("Idle is better than active."); }

    let previousHZT = (userData.logHeroSouls - 5) / Math.log10(1.25) * 5;
    let gilds = Math.max(1, Math.floor(previousHZT / 10) - 9);
    let baseHeroSouls = userData.logHeroSouls;
    userData.logHeroSouls += Math.log10(1 / 0.95) * userData.chorLevel - 2;

    let startingZone = 40;
    let timelapses = [];
    let zonesGained = 0;
    let rubyCost = 0;
    let currentHero;
    let revivedTLs = false;
    let logGold;
    
    if (userData.ascTime) {
        let endZone = getSoftCap(options, startingZone, logCps, logXylBonus, gilds)[0];
        let equivalentZones = userData.ascTime * 8050;
        if (userData.borbLimit && endZone > userData.borbLimit) {
            let remainder = endZone % 500;
            let mpz = Math.floor((endZone - userData.borbLimit) / 500) / 10 + 2;
            let monsters = (mpz - 2) * remainder / 1.083 + 1;
            if (monsters <= equivalentZones) {
                endZone -= remainder;
                equivalentZones -= monsters;
            } else {
                endZone -= (equivalentZones / monsters) * remainder;
                equivalentZones = 0;
            }
            mpz -= 0.1;
            while (mpz > 2) {
                let monsters = (mpz - 2) * 500 / 1.083 + 500;
                if (monsters <= equivalentZones) {
                    endZone -= 500;
                    equivalentZones -= monsters;
                } else {
                    endZone -= (equivalentZones / monsters) * 500;
                    equivalentZones = 0;
                    break;
                }
                mpz -= 0.1;
            }
        }
        endZone -= equivalentZones;
        userData.endZone = Math.max(1, Math.floor(endZone));
    }
    
    do {
        if (!revivedTLs) {
            logGold = getMonsterGold(startingZone, userData.logHeroSouls)
            let idleGoldExtra = startingZone > 140
                ? Math.log10(1.15 / 0.15)
                : Math.log10(1.6 / 0.6);
            idleGoldExtra += logXylBonus;
            let activeGoldExtra = logCps + 1;
            logGold += Math.max(idleGoldExtra, activeGoldExtra);
        }
        let IEsucks = findBestHero(logGold);
        let bestHero = IEsucks[0];
        let heroType = IEsucks[1];
        let heroLevel = getHeroLevel(logGold, bestHero, heroType);
        let heroDps = findHeroDps(bestHero, heroLevel, heroType, gilds);
        userData.highestZone = findHighestIdleZone(userData.logHeroSouls, heroDps, userData.xyliqilLevel, userData.autoClickers);
        userData.highestZone = userData.highestZone - userData.highestZone % 5 + 4;
        
        if (!revivedTLs) {
            currentHero = bestHero;
        }
        
        IEsucks = getNextTL(startingZone);
        if (IEsucks[0]) {
            if (bestHero === "Wepwawet2") { bestHero = "Wepwawet"; }
            zonesGained = IEsucks[1];
            timelapses.push({
                duration: IEsucks[0],
                bestHero: bestHero,
                heroLevel: heroLevel,
                zone: userData.highestZone,
                zoneDisplay: userData.highestZone.toLocaleString() + " (+" + IEsucks[1].toLocaleString() + ")",
            });
            rubyCost += IEsucks[2];
            startingZone = userData.highestZone;
            revivedTLs = false;
        } else {
            if (revivedTLs) {
                timelapses.pop();
                startingZone = timelapses[0] && timelapses[timelapses.length-1].zone || 40;;
                break;
            } else {
                if (userData.endZone) { break; }
                let IEsucks = findNextHero(bestHero);
                if (!IEsucks) { break; }
                let nextHero = IEsucks[0];
                zoneRequired = getZoneRequired(nextHero, useActive, logCps, logXylBonus);
                logGold = heroCosts[nextHero];
                if (zoneRequired >= userData.borbLimit) { break; }
                let softCap = getSoftCap(options, startingZone, logCps, logXylBonus, gilds)[0];
                if (zoneRequired >= softCap) { break; }
                revivedTLs = true;
                let zonesGained = zoneRequired - startingZone;
                if (zonesGained <= 0) { break; }
                let durationSeconds = Math.ceil(zonesGained / 8050 * 3600);
                let duration = formatTime(durationSeconds);
                timelapses.push({
                    duration: duration + " (wait)",
                    bestHero: bestHero,
                    heroLevel: heroLevel,
                    zone: zoneRequired,
                    zoneDisplay: zoneRequired.toLocaleString() + " (+" + zonesGained.toLocaleString() + ")",
                });
                startingZone = zoneRequired;
            }
        }
        if (userData.borbLimit && startingZone > (userData.borbLimit + 499)) { break; }
    } while (revivedTLs || zonesGained >= userData.minZones);

    userData.timelapseZoneMax = startingZone;
    
    let IEsucks = getSoftCap(options, startingZone, logCps, logXylBonus, gilds);
    let softCap = IEsucks[0];
    let bestHero = IEsucks[1];
    let heroLevel = IEsucks[2];
    
    let goldRequired = false;
    if (bestHero !== currentHero) {
        currentHero = bestHero;
        goldRequired = true;
    }
    
    let durationSeconds;
    if (userData.borbLimit && userData.highestZone > (userData.borbLimit + 499)) {
        if (userData.borbLimit > 0) {
            let flatZones = userData.borbLimit - userData.timelapseZoneMax;
            let n = userData.highestZone - userData.borbLimit;
            let highZones = n + (n * n) / 10830;
            let zonesTraveled = flatZones + highZones;
            durationSeconds = Math.ceil(zonesTraveled / 8050 * 3600);
        } else {
            let a = highestZone - userData.borbLimit;
            let zonesA = a + (a * a) * 10830;
            let b = -userData.borbLimit;
            let zonesB = b + (b * b) * 10830;
            let zonesTraveled = zonesA - zonesB;
            durationSeconds = Math.ceil(zonesTraveled / 8050 * 3600);
        }
    } else {
        let activeZonesGained = softCap - userData.timelapseZoneMax;
        durationSeconds = Math.ceil(activeZonesGained / 8050 * 3600);
    }
    let duration = formatTime(durationSeconds);
    if (bestHero === "Wepwawet2") { bestHero = "Wepwawet"; }
    timelapses.push({
        duration: duration,
        bestHero: bestHero,
        heroLevel: heroLevel,
        zone: userData.highestZone,
        zoneDisplay: userData.highestZone.toLocaleString() + " (max zone)",
    });

    // Test log
    if (options.test) {
        return (JSON.stringify({
            logHeroSouls: baseHeroSouls,
            xyliqilLevel: userData.xyliqilLevel,
            chorLevel: userData.chorLevel,
            autoClickers: userData.autoClickers,
            rubyCost: rubyCost,
            timelapses: timelapses,
        }));
    }

    // Display results
    let toappend = "";
    let t = 0;
    if (timelapses[4] && timelapses[4].duration === "168h") {
        for (let d = 4; d < timelapses.length; d++) {
            if (timelapses[d].duration === "168h") {
                t = d;
            }
        }
        timelapses[t].duration += " x" + (t + 1);
        timelapses[t].zoneDisplay = timelapses[t].zone.toLocaleString() + " (+" + (timelapses[t].zone - 40).toLocaleString() + ")";
    }
    for (t; t < timelapses.length; t++) {
        let row = timelapses[t];
        let heroLevel;
        if (row.heroLevel !== Infinity && row.heroLevel >= 1e21) {
            let s = row.heroLevel.toString();
            heroLevel = s.substr(0,5) + "e" + s.substr(s.indexOf("+"));
        } else {
            heroLevel = row.heroLevel.toLocaleString();
        }
        let title = "";
        if (t === (timelapses.length - 1)) {
            if (goldRequired) {
                let zoneRequired = getZoneRequired(currentHero, useActive, logCps, logXylBonus);
                if (zoneRequired <= userData.timelapseZoneMax) {
                    title = "Unlocked immediately after the last timelapse.";
                } else {
                    let zonesTraveled;
                    if (userData.borbLimit && (userData.borbLimit + 499) <= zoneRequired) {
                        let flatZones = userData.borbLimit - userData.timelapseZoneMax;
                        let n = zoneRequired - userData.borbLimit;
                        let highZones = n + (n * n) / 10830;
                        zonesTraveled = flatZones + highZones;
                    } else {
                        zonesTraveled = zoneRequired - userData.timelapseZoneMax;
                    }
                    
                    let hoursRequired = zonesTraveled / 8050;
                    let h = Math.floor(hoursRequired);
                    let m = Math.round((hoursRequired - h) * 60);
                    if (m < 10) m = "0" + m;
                    let time = h + ":" + m;
                    title = "Reachable at around zone " + zoneRequired.toLocaleString() + " which is " + time + " hours in.";
                }
            } else if (timelapses.length > 1 && timelapses[timelapses.length - 1]) {
                if (timelapses[timelapses.length - 2].bestHero === currentHero) {
                    title = "Unlocked during timelapses.";
                } else {
                    title = "Unlocked immediately after the last timelapse.";
                }
            }
        }
        toappend += "<tr title='" + title + "'><td>" + row.duration + "</td><td>" + row.bestHero + "</td><td>" + heroLevel + "</td><td>" + row.zoneDisplay + "</td>";
    }
    $("#TimelapsesTable tbody").html(toappend);
    $("#RubyCost").html("Total Rubies: " + rubyCost.toLocaleString());
    
    let numTLs = timelapses.length - 1;
    let altAction = false;
    userData.highestZone = timelapses[numTLs].zone;
    if (userData.data) {
        altAction = checkAncients();
    } else {
        $("#ancientCheckResults").parent().hide();
        $('html, body').animate({
            scrollTop: ($('#results').offset().top)
        },200);
    }
    
    // Recommended action
    let action;
    if (altAction) {
        action = altAction;
    } else if(numTLs === 0) {
        action = "Save your rubies.";
    } else if(previousHZT > 1e6) {
        action = "Use Timelapses as shown above.";
    } else if(userData.QAStrat === "perRuby"){
        let rubyCostTL = rubyCost - numTLs * 2; //consider mercenaries (estimated 2 rubies per TL)
        let maxZoneTL = timelapses[numTLs - 1].zone;
        let zonesPerRubyTL = maxZoneTL / rubyCostTL;
        let zonesPerRubyQA = previousHZT / 50;
        if(zonesPerRubyTL > zonesPerRubyQA) {
            action = "Use Timelapses as shown above.";
        } else {
            action = "Use Quick Ascension.";
        }
    } else {
        let maxZoneTL = timelapses[numTLs - 1].zone;
        if(maxZoneTL > previousHZT) {
            action = "Use Timelapses as shown above.";
        } else {
            action = "Use Quick Ascension.";
        }
    }
    $("#Recommend").html("Recommended: " + action);
}

function test() {
    let readout = "[\n";
    let options = {
        test: true,
        xyliqilLevel: 0,
        chorLevel: 0,
        autoClickers: 0,
        minZones: 20000,
        ascTime: 0
    }
    for (let i = 100; i < 2e5; i *= 2) {
        options.logHeroSouls = i;
        readout += "    " + refresh(options) + ",\n";
    }
    options.logHeroSouls = 1000;
    for (let i = 100; i < 1e7; i *= 10) {
        options.xyliqilLevel = i;
        readout += "    " + refresh(options) + ",\n";
    }
    options.xyliqilLevel = 0;
    for (let i = 50; i < 200; i += 50) {
        options.chorLevel = i;
        readout += "    " + refresh(options) + ",\n";
    }
    options.chorLevel = 0;
    for (let i = 1; i < 1e12; i *= 100) {
        options.autoClickers = i;
        readout += "    " + refresh(options) + ",\n";
    }
    readout = readout.slice(0, -2);
    readout += "\n]";
    $("#savegame").val(readout);
}

function enterKey(ev) {
    if (ev.which === 13) refresh();
}

function changeTheme() {
    if ($("#dark").is(":checked")) {
        $("#theme-light").prop("disabled", true);
        $("#theme-dark").prop("disabled", false);
    } else {
        $("#theme-light").prop("disabled", false);
        $("#theme-dark").prop("disabled", true);
    }
    if (localStorage) localStorage.setItem("darkmode", $("#dark").is(":checked"));
}

$(setDefaults);

$(function() {
    if (localStorage) {
        $("#dark").prop("checked", localStorage.getItem("darkmode")==="true");
    }

    $('.collapsible .title').click(function(){
        $(this).parent().find('.content').toggle();
    });
    
    $("#hero_souls").keyup(enterKey);

    $("#xyliqil_level").keyup(enterKey);

    $("#chor_level").keyup(enterKey);

    $("#autoclickers").keyup(enterKey);

    $("#minZones").keyup(enterKey);
    
    $("#ascTime").keyup(enterKey);
});