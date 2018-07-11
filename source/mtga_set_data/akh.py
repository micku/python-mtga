
import sys
from .models.card import Card
from .models.card_set import Set
import inspect


AngelofSanctions = Card("angel_of_sanctions", "Angel of Sanctions", ['3', 'W', 'W'], ['W'], "Creature", "Angel", "AKH", 1, 64801)
AnointedProcession = Card("anointed_procession", "Anointed Procession", ['3', 'W'], ['W'], "Enchantment", "", "AKH", 2, 64803)
AnointerPriest = Card("anointer_priest", "Anointer Priest", ['1', 'W'], ['W'], "Creature", "Human Cleric", "AKH", 3, 64805)
ApproachoftheSecondSun = Card("approach_of_the_second_sun", "Approach of the Second Sun", ['6', 'W'], ['W'], "Sorcery", "", "AKH", 4, 64807)
AvenMindcensor = Card("aven_mindcensor", "Aven Mindcensor", ['2', 'W'], ['W'], "Creature", "Bird Wizard", "AKH", 5, 64809)
BindingMummy = Card("binding_mummy", "Binding Mummy", ['1', 'W'], ['W'], "Creature", "Zombie", "AKH", 6, 64811)
CartoucheofSolidarity = Card("cartouche_of_solidarity", "Cartouche of Solidarity", ['W'], ['W'], "Enchantment", "Aura Cartouche", "AKH", 7, 64813)
CastOut = Card("cast_out", "Cast Out", ['3', 'W'], ['W'], "Enchantment", "", "AKH", 8, 64815)
CompulsoryRest = Card("compulsory_rest", "Compulsory Rest", ['1', 'W'], ['W'], "Enchantment", "Aura", "AKH", 9, 64817)
DevotedCropMate = Card("devoted_cropmate", "Devoted Crop-Mate", ['2', 'W'], ['W'], "Creature", "Human Warrior", "AKH", 10, 64819)
DjerusResolve = Card("djerus_resolve", "Djeru's Resolve", ['W'], ['W'], "Instant", "", "AKH", 11, 64821)
FanBearer = Card("fan_bearer", "Fan Bearer", ['W'], ['W'], "Creature", "Zombie", "AKH", 12, 64823)
ForsaketheWorldly = Card("forsake_the_worldly", "Forsake the Worldly", ['2', 'W'], ['W'], "Instant", "", "AKH", 13, 64825)
GideonoftheTrials = Card("gideon_of_the_trials", "Gideon of the Trials", ['1', 'W', 'W'], ['W'], "Legendary Planeswalker", "Gideon", "AKH", 14, 64827)
GideonsIntervention = Card("gideons_intervention", "Gideon's Intervention", ['2', 'W', 'W'], ['W'], "Enchantment", "", "AKH", 15, 64829)
GloryBoundInitiate = Card("glorybound_initiate", "Glory-Bound Initiate", ['1', 'W'], ['W'], "Creature", "Human Warrior", "AKH", 16, 64831)
GustWalker = Card("gust_walker", "Gust Walker", ['1', 'W'], ['W'], "Creature", "Human Wizard", "AKH", 17, 64833)
ImpeccableTiming = Card("impeccable_timing", "Impeccable Timing", ['1', 'W'], ['W'], "Instant", "", "AKH", 18, 64835)
InOketrasName = Card("in_oketras_name", "In Oketra's Name", ['1', 'W'], ['W'], "Instant", "", "AKH", 19, 64837)
MightyLeap = Card("mighty_leap", "Mighty Leap", ['1', 'W'], ['W'], "Instant", "", "AKH", 20, 64839)
OketratheTrue = Card("oketra_the_true", "Oketra the True", ['3', 'W'], ['W'], "Legendary Creature", "God", "AKH", 21, 64841)
OketrasAttendant = Card("oketras_attendant", "Oketra's Attendant", ['3', 'W', 'W'], ['W'], "Creature", "Bird Soldier", "AKH", 22, 64843)
ProtectionoftheHekma = Card("protection_of_the_hekma", "Protection of the Hekma", ['4', 'W'], ['W'], "Enchantment", "", "AKH", 23, 64845)
RegalCaracal = Card("regal_caracal", "Regal Caracal", ['3', 'W', 'W'], ['W'], "Creature", "Cat", "AKH", 24, 64847)
RenewedFaith = Card("renewed_faith", "Renewed Faith", ['2', 'W'], ['W'], "Instant", "", "AKH", 25, 64849)
RhetCropSpearmaster = Card("rhetcrop_spearmaster", "Rhet-Crop Spearmaster", ['2', 'W'], ['W'], "Creature", "Human Warrior", "AKH", 26, 64851)
SacredCat = Card("sacred_cat", "Sacred Cat", ['W'], ['W'], "Creature", "Cat", "AKH", 27, 64853)
SeraphoftheSuns = Card("seraph_of_the_suns", "Seraph of the Suns", ['5', 'W', 'W'], ['W'], "Creature", "Angel", "AKH", 28, 64855)
SparringMummy = Card("sparring_mummy", "Sparring Mummy", ['3', 'W'], ['W'], "Creature", "Zombie", "AKH", 29, 64857)
SupplyCaravan = Card("supply_caravan", "Supply Caravan", ['4', 'W'], ['W'], "Creature", "Camel", "AKH", 30, 64859)
TahCropElite = Card("tahcrop_elite", "Tah-Crop Elite", ['3', 'W'], ['W'], "Creature", "Bird Warrior", "AKH", 31, 64861)
ThoseWhoServe = Card("those_who_serve", "Those Who Serve", ['2', 'W'], ['W'], "Creature", "Zombie", "AKH", 32, 64863)
TimetoReflect = Card("time_to_reflect", "Time to Reflect", ['W'], ['W'], "Instant", "", "AKH", 33, 64865)
TrialofSolidarity = Card("trial_of_solidarity", "Trial of Solidarity", ['2', 'W'], ['W'], "Enchantment", "", "AKH", 34, 64867)
TrueheartDuelist = Card("trueheart_duelist", "Trueheart Duelist", ['1', 'W'], ['W'], "Creature", "Human Warrior", "AKH", 35, 64869)
UnwaveringInitiate = Card("unwavering_initiate", "Unwavering Initiate", ['2', 'W'], ['W'], "Creature", "Human Warrior", "AKH", 36, 64871)
VizierofDeferment = Card("vizier_of_deferment", "Vizier of Deferment", ['2', 'W'], ['W'], "Creature", "Human Cleric", "AKH", 37, 64873)
VizierofRemedies = Card("vizier_of_remedies", "Vizier of Remedies", ['1', 'W'], ['W'], "Creature", "Human Cleric", "AKH", 38, 64875)
WingedShepherd = Card("winged_shepherd", "Winged Shepherd", ['5', 'W'], ['W'], "Creature", "Angel", "AKH", 39, 64877)
AncientCrab = Card("ancient_crab", "Ancient Crab", ['1', 'U', 'U'], ['U'], "Creature", "Crab", "AKH", 40, 64879)
AnglerDrake = Card("angler_drake", "Angler Drake", ['4', 'U', 'U'], ['U'], "Creature", "Drake", "AKH", 41, 64881)
AsForetold = Card("as_foretold", "As Foretold", ['2', 'U'], ['U'], "Enchantment", "", "AKH", 42, 64883)
AvenInitiate = Card("aven_initiate", "Aven Initiate", ['3', 'U'], ['U'], "Creature", "Bird Warrior", "AKH", 43, 64885)
Cancel = Card("cancel", "Cancel", ['1', 'U', 'U'], ['U'], "Instant", "", "AKH", 44, 64887)
CartoucheofKnowledge = Card("cartouche_of_knowledge", "Cartouche of Knowledge", ['1', 'U'], ['U'], "Enchantment", "Aura Cartouche", "AKH", 45, 64889)
Censor = Card("censor", "Censor", ['1', 'U'], ['U'], "Instant", "", "AKH", 46, 64891)
CompellingArgument = Card("compelling_argument", "Compelling Argument", ['1', 'U'], ['U'], "Sorcery", "", "AKH", 47, 64893)
CrypticSerpent = Card("cryptic_serpent", "Cryptic Serpent", ['5', 'U', 'U'], ['U'], "Creature", "Serpent", "AKH", 48, 64895)
CuratorofMysteries = Card("curator_of_mysteries", "Curator of Mysteries", ['2', 'U', 'U'], ['U'], "Creature", "Sphinx", "AKH", 49, 64897)
DecisionParalysis = Card("decision_paralysis", "Decision Paralysis", ['3', 'U'], ['U'], "Instant", "", "AKH", 50, 64899)
DrakeHaven = Card("drake_haven", "Drake Haven", ['2', 'U'], ['U'], "Enchantment", "", "AKH", 51, 64901)
EssenceScatter = Card("essence_scatter", "Essence Scatter", ['1', 'U'], ['U'], "Instant", "", "AKH", 52, 64903)
Floodwaters = Card("floodwaters", "Floodwaters", ['4', 'U', 'U'], ['U'], "Sorcery", "", "AKH", 53, 64905)
Galestrike = Card("galestrike", "Galestrike", ['2', 'U'], ['U'], "Instant", "", "AKH", 54, 64907)
GlyphKeeper = Card("glyph_keeper", "Glyph Keeper", ['3', 'U', 'U'], ['U'], "Creature", "Sphinx", "AKH", 55, 64909)
HekmaSentinels = Card("hekma_sentinels", "Hekma Sentinels", ['2', 'U'], ['U'], "Creature", "Human Cleric", "AKH", 56, 64911)
HieroglyphicIllumination = Card("hieroglyphic_illumination", "Hieroglyphic Illumination", ['3', 'U'], ['U'], "Instant", "", "AKH", 57, 64913)
IllusoryWrappings = Card("illusory_wrappings", "Illusory Wrappings", ['2', 'U'], ['U'], "Enchantment", "Aura", "AKH", 58, 64915)
KefnettheMindful = Card("kefnet_the_mindful", "Kefnet the Mindful", ['2', 'U'], ['U'], "Legendary Creature", "God", "AKH", 59, 64917)
LabyrinthGuardian = Card("labyrinth_guardian", "Labyrinth Guardian", ['1', 'U'], ['U'], "Creature", "Illusion Warrior", "AKH", 60, 64919)
LayClaim = Card("lay_claim", "Lay Claim", ['5', 'U', 'U'], ['U'], "Enchantment", "Aura", "AKH", 61, 64921)
NagaOracle = Card("naga_oracle", "Naga Oracle", ['3', 'U'], ['U'], "Creature", "Naga Cleric", "AKH", 62, 64923)
NewPerspectives = Card("new_perspectives", "New Perspectives", ['5', 'U'], ['U'], "Enchantment", "", "AKH", 63, 64925)
OpenintoWonder = Card("open_into_wonder", "Open into Wonder", ['X', 'U', 'U'], ['U'], "Sorcery", "", "AKH", 64, 64927)
PullfromTomorrow = Card("pull_from_tomorrow", "Pull from Tomorrow", ['X', 'U', 'U'], ['U'], "Instant", "", "AKH", 65, 64929)
RiverSerpent = Card("river_serpent", "River Serpent", ['5', 'U'], ['U'], "Creature", "Serpent", "AKH", 66, 64931)
SacredExcavation = Card("sacred_excavation", "Sacred Excavation", ['3', 'U'], ['U'], "Sorcery", "", "AKH", 67, 64933)
ScribeoftheMindful = Card("scribe_of_the_mindful", "Scribe of the Mindful", ['2', 'U'], ['U'], "Creature", "Human Cleric", "AKH", 68, 64935)
SeekerofInsight = Card("seeker_of_insight", "Seeker of Insight", ['1', 'U'], ['U'], "Creature", "Human Wizard", "AKH", 69, 64937)
ShimmerscaleDrake = Card("shimmerscale_drake", "Shimmerscale Drake", ['4', 'U'], ['U'], "Creature", "Drake", "AKH", 70, 64939)
SlitherBlade = Card("slither_blade", "Slither Blade", ['U'], ['U'], "Creature", "Naga Rogue", "AKH", 71, 64941)
TahCropSkirmisher = Card("tahcrop_skirmisher", "Tah-Crop Skirmisher", ['1', 'U'], ['U'], "Creature", "Naga Warrior", "AKH", 72, 64943)
TrialofKnowledge = Card("trial_of_knowledge", "Trial of Knowledge", ['3', 'U'], ['U'], "Enchantment", "", "AKH", 73, 64945)
VizierofManyFaces = Card("vizier_of_many_faces", "Vizier of Many Faces", ['2', 'U', 'U'], ['U'], "Creature", "Shapeshifter Cleric", "AKH", 74, 64947)
VizierofTumblingSands = Card("vizier_of_tumbling_sands", "Vizier of Tumbling Sands", ['2', 'U'], ['U'], "Creature", "Human Cleric", "AKH", 75, 64949)
WindsofRebuke = Card("winds_of_rebuke", "Winds of Rebuke", ['1', 'U'], ['U'], "Instant", "", "AKH", 76, 64951)
ZenithSeeker = Card("zenith_seeker", "Zenith Seeker", ['3', 'U'], ['U'], "Creature", "Bird Wizard", "AKH", 77, 64953)
ArchfiendofIfnir = Card("archfiend_of_ifnir", "Archfiend of Ifnir", ['3', 'B', 'B'], ['B'], "Creature", "Demon", "AKH", 78, 64955)
BalefulAmmit = Card("baleful_ammit", "Baleful Ammit", ['2', 'B'], ['B'], "Creature", "Crocodile Demon", "AKH", 79, 64957)
BlightedBat = Card("blighted_bat", "Blighted Bat", ['2', 'B'], ['B'], "Creature", "Zombie Bat", "AKH", 80, 64959)
BonePicker = Card("bone_picker", "Bone Picker", ['3', 'B'], ['B'], "Creature", "Bird", "AKH", 81, 64961)
BontutheGlorified = Card("bontu_the_glorified", "Bontu the Glorified", ['2', 'B'], ['B'], "Legendary Creature", "God", "AKH", 82, 64963)
CartoucheofAmbition = Card("cartouche_of_ambition", "Cartouche of Ambition", ['2', 'B'], ['B'], "Enchantment", "Aura Cartouche", "AKH", 83, 64965)
CruelReality = Card("cruel_reality", "Cruel Reality", ['5', 'B', 'B'], ['B'], "Enchantment", "Aura Curse", "AKH", 84, 64967)
CursedMinotaur = Card("cursed_minotaur", "Cursed Minotaur", ['2', 'B'], ['B'], "Creature", "Zombie Minotaur", "AKH", 85, 64969)
Dispossess = Card("dispossess", "Dispossess", ['2', 'B'], ['B'], "Sorcery", "", "AKH", 86, 64971)
DoomedDissenter = Card("doomed_dissenter", "Doomed Dissenter", ['1', 'B'], ['B'], "Creature", "Human", "AKH", 87, 64973)
DreadWanderer = Card("dread_wanderer", "Dread Wanderer", ['B'], ['B'], "Creature", "Zombie Jackal", "AKH", 88, 64975)
DuneBeetle = Card("dune_beetle", "Dune Beetle", ['1', 'B'], ['B'], "Creature", "Insect", "AKH", 89, 64977)
FaithoftheDevoted = Card("faith_of_the_devoted", "Faith of the Devoted", ['2', 'B'], ['B'], "Enchantment", "", "AKH", 90, 64979)
FesteringMummy = Card("festering_mummy", "Festering Mummy", ['B'], ['B'], "Creature", "Zombie", "AKH", 91, 64981)
FinalReward = Card("final_reward", "Final Reward", ['4', 'B'], ['B'], "Instant", "", "AKH", 92, 64983)
Gravedigger = Card("gravedigger", "Gravedigger", ['3', 'B'], ['B'], "Creature", "Zombie", "AKH", 93, 64985)
GrimStrider = Card("grim_strider", "Grim Strider", ['3', 'B'], ['B'], "Creature", "Horror", "AKH", 94, 64987)
HorroroftheBrokenLands = Card("horror_of_the_broken_lands", "Horror of the Broken Lands", ['4', 'B'], ['B'], "Creature", "Horror", "AKH", 95, 64989)
LayBaretheHeart = Card("lay_bare_the_heart", "Lay Bare the Heart", ['1', 'B'], ['B'], "Sorcery", "", "AKH", 96, 64991)
LilianaDeathsMajesty = Card("liliana_deaths_majesty", "Liliana, Death's Majesty", ['3', 'B', 'B'], ['B'], "Legendary Planeswalker", "Liliana", "AKH", 97, 64993)
LilianasMastery = Card("lilianas_mastery", "Liliana's Mastery", ['3', 'B', 'B'], ['B'], "Enchantment", "", "AKH", 98, 64995)
LordoftheAccursed = Card("lord_of_the_accursed", "Lord of the Accursed", ['2', 'B'], ['B'], "Creature", "Zombie", "AKH", 99, 64997)
MiasmicMummy = Card("miasmic_mummy", "Miasmic Mummy", ['1', 'B'], ['B'], "Creature", "Zombie Jackal", "AKH", 100, 64999)
NestofScarabs = Card("nest_of_scarabs", "Nest of Scarabs", ['2', 'B'], ['B'], "Enchantment", "", "AKH", 101, 65001)
PainfulLesson = Card("painful_lesson", "Painful Lesson", ['2', 'B'], ['B'], "Sorcery", "", "AKH", 102, 65003)
PitilessVizier = Card("pitiless_vizier", "Pitiless Vizier", ['3', 'B'], ['B'], "Creature", "Minotaur Cleric", "AKH", 103, 65005)
PlagueBelcher = Card("plague_belcher", "Plague Belcher", ['2', 'B'], ['B'], "Creature", "Zombie Beast", "AKH", 104, 65007)
RuthlessSniper = Card("ruthless_sniper", "Ruthless Sniper", ['B'], ['B'], "Creature", "Human Archer", "AKH", 105, 65009)
ScarabFeast = Card("scarab_feast", "Scarab Feast", ['B'], ['B'], "Instant", "", "AKH", 106, 65011)
ShadowoftheGrave = Card("shadow_of_the_grave", "Shadow of the Grave", ['1', 'B'], ['B'], "Instant", "", "AKH", 107, 65013)
Soulstinger = Card("soulstinger", "Soulstinger", ['3', 'B'], ['B'], "Creature", "Scorpion Demon", "AKH", 108, 65015)
SplendidAgony = Card("splendid_agony", "Splendid Agony", ['2', 'B'], ['B'], "Instant", "", "AKH", 109, 65017)
StirtheSands = Card("stir_the_sands", "Stir the Sands", ['4', 'B', 'B'], ['B'], "Sorcery", "", "AKH", 110, 65019)
SupernaturalStamina = Card("supernatural_stamina", "Supernatural Stamina", ['B'], ['B'], "Instant", "", "AKH", 111, 65021)
TrespassersCurse = Card("trespassers_curse", "Trespasser's Curse", ['1', 'B'], ['B'], "Enchantment", "Aura Curse", "AKH", 112, 65023)
TrialofAmbition = Card("trial_of_ambition", "Trial of Ambition", ['1', 'B'], ['B'], "Enchantment", "", "AKH", 113, 65025)
Unburden = Card("unburden", "Unburden", ['1', 'B', 'B'], ['B'], "Sorcery", "", "AKH", 114, 65027)
WanderinDeath = Card("wander_in_death", "Wander in Death", ['2', 'B'], ['B'], "Sorcery", "", "AKH", 115, 65029)
WastelandScorpion = Card("wasteland_scorpion", "Wasteland Scorpion", ['2', 'B'], ['B'], "Creature", "Scorpion", "AKH", 116, 65031)
AhnCropCrasher = Card("ahncrop_crasher", "Ahn-Crop Crasher", ['2', 'R'], ['R'], "Creature", "Minotaur Warrior", "AKH", 117, 65033)
BattlefieldScavenger = Card("battlefield_scavenger", "Battlefield Scavenger", ['1', 'R'], ['R'], "Creature", "Jackal Rogue", "AKH", 118, 65035)
BlazingVolley = Card("blazing_volley", "Blazing Volley", ['R'], ['R'], "Sorcery", "", "AKH", 119, 65037)
BloodlustInciter = Card("bloodlust_inciter", "Bloodlust Inciter", ['R'], ['R'], "Creature", "Human Warrior", "AKH", 120, 65039)
BloodrageBrawler = Card("bloodrage_brawler", "Bloodrage Brawler", ['1', 'R'], ['R'], "Creature", "Minotaur Warrior", "AKH", 121, 65041)
BruteStrength = Card("brute_strength", "Brute Strength", ['1', 'R'], ['R'], "Instant", "", "AKH", 122, 65043)
ByForce = Card("by_force", "By Force", ['X', 'R'], ['R'], "Sorcery", "", "AKH", 123, 65045)
CartoucheofZeal = Card("cartouche_of_zeal", "Cartouche of Zeal", ['R'], ['R'], "Enchantment", "Aura Cartouche", "AKH", 124, 65047)
CombatCelebrant = Card("combat_celebrant", "Combat Celebrant", ['2', 'R'], ['R'], "Creature", "Human Warrior", "AKH", 125, 65049)
ConsumingFervor = Card("consuming_fervor", "Consuming Fervor", ['R'], ['R'], "Enchantment", "Aura", "AKH", 126, 65051)
DeemWorthy = Card("deem_worthy", "Deem Worthy", ['4', 'R'], ['R'], "Instant", "", "AKH", 127, 65053)
DesertCerodon = Card("desert_cerodon", "Desert Cerodon", ['5', 'R'], ['R'], "Creature", "Beast", "AKH", 128, 65055)
Electrify = Card("electrify", "Electrify", ['3', 'R'], ['R'], "Instant", "", "AKH", 129, 65057)
EmberhornMinotaur = Card("emberhorn_minotaur", "Emberhorn Minotaur", ['3', 'R'], ['R'], "Creature", "Minotaur Warrior", "AKH", 130, 65059)
FlamebladeAdept = Card("flameblade_adept", "Flameblade Adept", ['R'], ['R'], "Creature", "Jackal Warrior", "AKH", 131, 65061)
Fling = Card("fling", "Fling", ['1', 'R'], ['R'], "Instant", "", "AKH", 132, 65063)
GloriousEnd = Card("glorious_end", "Glorious End", ['2', 'R'], ['R'], "Instant", "", "AKH", 133, 65065)
Glorybringer = Card("glorybringer", "Glorybringer", ['3', 'R', 'R'], ['R'], "Creature", "Dragon", "AKH", 134, 65067)
HarshMentor = Card("harsh_mentor", "Harsh Mentor", ['1', 'R'], ['R'], "Creature", "Human Cleric", "AKH", 135, 65069)
HazorettheFervent = Card("hazoret_the_fervent", "Hazoret the Fervent", ['3', 'R'], ['R'], "Legendary Creature", "God", "AKH", 136, 65071)
HazoretsFavor = Card("hazorets_favor", "Hazoret's Favor", ['2', 'R'], ['R'], "Enchantment", "", "AKH", 137, 65073)
HeartPiercerManticore = Card("heartpiercer_manticore", "Heart-Piercer Manticore", ['2', 'R', 'R'], ['R'], "Creature", "Manticore", "AKH", 138, 65075)
HyenaPack = Card("hyena_pack", "Hyena Pack", ['2', 'R', 'R'], ['R'], "Creature", "Hyena", "AKH", 139, 65077)
LimitsofSolidarity = Card("limits_of_solidarity", "Limits of Solidarity", ['3', 'R'], ['R'], "Sorcery", "", "AKH", 140, 65079)
MagmaSpray = Card("magma_spray", "Magma Spray", ['R'], ['R'], "Instant", "", "AKH", 141, 65081)
ManticoreoftheGauntlet = Card("manticore_of_the_gauntlet", "Manticore of the Gauntlet", ['4', 'R'], ['R'], "Creature", "Manticore", "AKH", 142, 65083)
MinotaurSureshot = Card("minotaur_sureshot", "Minotaur Sureshot", ['2', 'R'], ['R'], "Creature", "Minotaur Archer", "AKH", 143, 65085)
NefCropEntangler = Card("nefcrop_entangler", "Nef-Crop Entangler", ['1', 'R'], ['R'], "Creature", "Human Warrior", "AKH", 144, 65087)
NimbleBladeKhenra = Card("nimbleblade_khenra", "Nimble-Blade Khenra", ['1', 'R'], ['R'], "Creature", "Jackal Warrior", "AKH", 145, 65089)
PathmakerInitiate = Card("pathmaker_initiate", "Pathmaker Initiate", ['1', 'R'], ['R'], "Creature", "Human Wizard", "AKH", 146, 65091)
PursueGlory = Card("pursue_glory", "Pursue Glory", ['3', 'R'], ['R'], "Instant", "", "AKH", 147, 65093)
SoulScarMage = Card("soulscar_mage", "Soul-Scar Mage", ['R'], ['R'], "Creature", "Human Wizard", "AKH", 148, 65095)
SwelteringSuns = Card("sweltering_suns", "Sweltering Suns", ['1', 'R', 'R'], ['R'], "Sorcery", "", "AKH", 149, 65097)
ThresherLizard = Card("thresher_lizard", "Thresher Lizard", ['2', 'R'], ['R'], "Creature", "Lizard", "AKH", 150, 65099)
TormentingVoice = Card("tormenting_voice", "Tormenting Voice", ['1', 'R'], ['R'], "Sorcery", "", "AKH", 151, 65101)
TrialofZeal = Card("trial_of_zeal", "Trial of Zeal", ['2', 'R'], ['R'], "Enchantment", "", "AKH", 152, 65103)
TrueheartTwins = Card("trueheart_twins", "Trueheart Twins", ['4', 'R'], ['R'], "Creature", "Jackal Warrior", "AKH", 153, 65105)
ViolentImpact = Card("violent_impact", "Violent Impact", ['3', 'R'], ['R'], "Sorcery", "", "AKH", 154, 65107)
WarfireJavelineer = Card("warfire_javelineer", "Warfire Javelineer", ['3', 'R'], ['R'], "Creature", "Minotaur Warrior", "AKH", 155, 65109)
BenefactionofRhonas = Card("benefaction_of_rhonas", "Benefaction of Rhonas", ['2', 'G'], ['G'], "Sorcery", "", "AKH", 156, 65111)
BitterbladeWarrior = Card("bitterblade_warrior", "Bitterblade Warrior", ['1', 'G'], ['G'], "Creature", "Jackal Warrior", "AKH", 157, 65113)
CartoucheofStrength = Card("cartouche_of_strength", "Cartouche of Strength", ['2', 'G'], ['G'], "Enchantment", "Aura Cartouche", "AKH", 158, 65115)
ChampionofRhonas = Card("champion_of_rhonas", "Champion of Rhonas", ['3', 'G'], ['G'], "Creature", "Jackal Warrior", "AKH", 159, 65117)
ChannelerInitiate = Card("channeler_initiate", "Channeler Initiate", ['1', 'G'], ['G'], "Creature", "Human Druid", "AKH", 160, 65119)
Colossapede = Card("colossapede", "Colossapede", ['4', 'G'], ['G'], "Creature", "Insect", "AKH", 161, 65121)
CrocodileoftheCrossing = Card("crocodile_of_the_crossing", "Crocodile of the Crossing", ['3', 'G'], ['G'], "Creature", "Crocodile", "AKH", 162, 65123)
DefiantGreatmaw = Card("defiant_greatmaw", "Defiant Greatmaw", ['2', 'G'], ['G'], "Creature", "Hippo", "AKH", 163, 65125)
DissentersDeliverance = Card("dissenters_deliverance", "Dissenter's Deliverance", ['1', 'G'], ['G'], "Instant", "", "AKH", 164, 65127)
ExemplarofStrength = Card("exemplar_of_strength", "Exemplar of Strength", ['1', 'G'], ['G'], "Creature", "Human Warrior", "AKH", 165, 65129)
GiantSpider = Card("giant_spider", "Giant Spider", ['3', 'G'], ['G'], "Creature", "Spider", "AKH", 166, 65131)
GiftofParadise = Card("gift_of_paradise", "Gift of Paradise", ['2', 'G'], ['G'], "Enchantment", "Aura", "AKH", 167, 65133)
GreaterSandwurm = Card("greater_sandwurm", "Greater Sandwurm", ['5', 'G', 'G'], ['G'], "Creature", "Wurm", "AKH", 168, 65135)
HapatrasMark = Card("hapatras_mark", "Hapatra's Mark", ['G'], ['G'], "Instant", "", "AKH", 169, 65137)
HarvestSeason = Card("harvest_season", "Harvest Season", ['2', 'G'], ['G'], "Sorcery", "", "AKH", 170, 65139)
# start mixup
HazeofPollen = Card("haze_of_pollen", "Haze of Pollen", ['1', 'G'], ['G'], "Instant", "", "AKH", 171, 65427)
HonoredHydra = Card("honored_hydra", "Honored Hydra", ['5', 'G'], ['G'], "Creature", "Snake Hydra", "AKH", 172, 65141)
HoodedBrawler = Card("hooded_brawler", "Hooded Brawler", ['2', 'G'], ['G'], "Creature", "Naga Warrior", "AKH", 173, 65143)
InitiatesCompanion = Card("initiates_companion", "Initiate's Companion", ['1', 'G'], ['G'], "Creature", "Cat", "AKH", 174, 65145)
# end mixup
Manglehorn = Card("manglehorn", "Manglehorn", ['2', 'G'], ['G'], "Creature", "Beast", "AKH", 175, 65149)
NagaVitalist = Card("naga_vitalist", "Naga Vitalist", ['1', 'G'], ['G'], "Creature", "Naga Druid", "AKH", 176, 65151)
OashraCultivator = Card("oashra_cultivator", "Oashra Cultivator", ['G'], ['G'], "Creature", "Human Druid", "AKH", 177, 65153)
OrneryKudu = Card("ornery_kudu", "Ornery Kudu", ['2', 'G'], ['G'], "Creature", "Antelope", "AKH", 178, 65155)
PouncingCheetah = Card("pouncing_cheetah", "Pouncing Cheetah", ['2', 'G'], ['G'], "Creature", "Cat", "AKH", 179, 65157)
ProwlingSerpopard = Card("prowling_serpopard", "Prowling Serpopard", ['1', 'G', 'G'], ['G'], "Creature", "Cat Snake", "AKH", 180, 65159)
QuarryHauler = Card("quarry_hauler", "Quarry Hauler", ['3', 'G'], ['G'], "Creature", "Camel", "AKH", 181, 65161)
RhonastheIndomitable = Card("rhonas_the_indomitable", "Rhonas the Indomitable", ['2', 'G'], ['G'], "Legendary Creature", "God", "AKH", 182, 65163)
SandwurmConvergence = Card("sandwurm_convergence", "Sandwurm Convergence", ['6', 'G', 'G'], ['G'], "Enchantment", "", "AKH", 183, 65165)
ScaledBehemoth = Card("scaled_behemoth", "Scaled Behemoth", ['4', 'G', 'G'], ['G'], "Creature", "Crocodile", "AKH", 184, 65167)
ShedWeakness = Card("shed_weakness", "Shed Weakness", ['G'], ['G'], "Instant", "", "AKH", 185, 65169)
ShefetMonitor = Card("shefet_monitor", "Shefet Monitor", ['5', 'G'], ['G'], "Creature", "Lizard", "AKH", 186, 65171)
SixthSense = Card("sixth_sense", "Sixth Sense", ['G'], ['G'], "Enchantment", "Aura", "AKH", 187, 65173)
SpideryGrasp = Card("spidery_grasp", "Spidery Grasp", ['2', 'G'], ['G'], "Instant", "", "AKH", 188, 65175)
StingingShot = Card("stinging_shot", "Stinging Shot", ['G'], ['G'], "Instant", "", "AKH", 189, 65177)
SynchronizedStrike = Card("synchronized_strike", "Synchronized Strike", ['2', 'G'], ['G'], "Instant", "", "AKH", 190, 65179)
TrialofStrength = Card("trial_of_strength", "Trial of Strength", ['2', 'G'], ['G'], "Enchantment", "", "AKH", 191, 65181)
VizieroftheMenagerie = Card("vizier_of_the_menagerie", "Vizier of the Menagerie", ['3', 'G'], ['G'], "Creature", "Naga Cleric", "AKH", 192, 65183)
WatchfulNaga = Card("watchful_naga", "Watchful Naga", ['2', 'G'], ['G'], "Creature", "Naga Wizard", "AKH", 193, 65185)
AhnCropChampion = Card("ahncrop_champion", "Ahn-Crop Champion", ['2', 'G', 'W'], ['W', 'G'], "Creature", "Human Warrior", "AKH", 194, 65187)
AvenWindGuide = Card("aven_wind_guide", "Aven Wind Guide", ['2', 'W', 'U'], ['W', 'U'], "Creature", "Bird Warrior", "AKH", 195, 65189)
BountyoftheLuxa = Card("bounty_of_the_luxa", "Bounty of the Luxa", ['2', 'G', 'U'], ['U', 'G'], "Enchantment", "", "AKH", 196, 65191)
DecimatorBeetle = Card("decimator_beetle", "Decimator Beetle", ['3', 'B', 'G'], ['B', 'G'], "Creature", "Insect", "AKH", 197, 65193)
EnigmaDrake = Card("enigma_drake", "Enigma Drake", ['1', 'U', 'R'], ['U', 'R'], "Creature", "Drake", "AKH", 198, 65195)
HapatraVizierofPoisons = Card("hapatra_vizier_of_poisons", "Hapatra, Vizier of Poisons", ['B', 'G'], ['B', 'G'], "Legendary Creature", "Human Cleric", "AKH", 199, 65197)
HonoredCropCaptain = Card("honored_cropcaptain", "Honored Crop-Captain", ['R', 'W'], ['W', 'R'], "Creature", "Human Warrior", "AKH", 200, 65199)
KhenraCharioteer = Card("khenra_charioteer", "Khenra Charioteer", ['1', 'R', 'G'], ['R', 'G'], "Creature", "Jackal Warrior", "AKH", 201, 65201)
MercilessJavelineer = Card("merciless_javelineer", "Merciless Javelineer", ['2', 'B', 'R'], ['B', 'R'], "Creature", "Minotaur Warrior", "AKH", 202, 65203)
NehebtheWorthy = Card("neheb_the_worthy", "Neheb, the Worthy", ['1', 'B', 'R'], ['B', 'R'], "Legendary Creature", "Minotaur Warrior", "AKH", 203, 65205)
NissaStewardofElements = Card("nissa_steward_of_elements", "Nissa, Steward of Elements", ['X', 'G', 'U'], ['U', 'G'], "Legendary Planeswalker", "Nissa", "AKH", 204, 65207)
SamutVoiceofDissent = Card("samut_voice_of_dissent", "Samut, Voice of Dissent", ['3', 'R', 'G'], ['R', 'G', 'W'], "Legendary Creature", "Human Warrior", "AKH", 205, 65209)
ShadowstormVizier = Card("shadowstorm_vizier", "Shadowstorm Vizier", ['U', 'B'], ['U', 'B'], "Creature", "Human Cleric", "AKH", 206, 65211)
TemmetVizierofNaktamun = Card("temmet_vizier_of_naktamun", "Temmet, Vizier of Naktamun", ['W', 'U'], ['W', 'U'], "Legendary Creature", "Human Cleric", "AKH", 207, 65213)
WaywardServant = Card("wayward_servant", "Wayward Servant", ['W', 'B'], ['W', 'B'], "Creature", "Zombie", "AKH", 208, 65215)
WeaverofCurrents = Card("weaver_of_currents", "Weaver of Currents", ['1', 'G', 'U'], ['U', 'G'], "Creature", "Naga Druid", "AKH", 209, 65217)
Dusk = Card("dusk", "Dusk", ['2', 'W', 'W'], ['W'], "Sorcery", "", "AKH", 210, 65219)
Dawn = Card("dawn", "Dawn", ['3', 'W', 'W'], ['W'], "Sorcery", "", "AKH", 210, 65222)
Commit = Card("commit", "Commit", ['3', 'U'], ['U'], "Instant", "", "AKH", 211, 65225)
Memory = Card("memory", "Memory", ['4', 'U', 'U'], ['U'], "Sorcery", "", "AKH", 211, 65228)
Never = Card("never", "Never", ['1', 'B', 'B'], ['B'], "Sorcery", "", "AKH", 212, 65231)
Return = Card("return", "Return", ['3', 'B'], ['B'], "Sorcery", "", "AKH", 212, 65234)
Insult = Card("insult", "Insult", ['2', 'R'], ['R'], "Sorcery", "", "AKH", 213, 65237)
Injury = Card("injury", "Injury", ['2', 'R'], ['R'], "Sorcery", "", "AKH", 213, 65240)
Mouth = Card("mouth", "Mouth", ['2', 'G'], ['G'], "Sorcery", "", "AKH", 214, 65243)
Feed = Card("feed", "Feed", ['3', 'G'], ['G'], "Sorcery", "", "AKH", 214, 65246)
Start = Card("start", "Start", ['2', 'W'], ['W', 'B'], "Instant", "", "AKH", 215, 65249)
Finish = Card("finish", "Finish", ['2', 'B'], ['W', 'B'], "Sorcery", "", "AKH", 215, 65252)
Reduce = Card("reduce", "Reduce", ['2', 'U'], ['R', 'U'], "Instant", "", "AKH", 216, 65255)
Rubble = Card("rubble", "Rubble", ['2', 'R'], ['R', 'U'], "Sorcery", "", "AKH", 216, 65258)
Destined = Card("destined", "Destined", ['1', 'B'], ['G', 'B'], "Instant", "", "AKH", 217, 65261)
Lead = Card("lead", "Lead", ['3', 'G'], ['G', 'B'], "Sorcery", "", "AKH", 217, 65264)
Onward = Card("onward", "Onward", ['2', 'R'], ['W', 'R'], "Instant", "", "AKH", 218, 65267)
Victory = Card("victory", "Victory", ['2', 'W'], ['W', 'R'], "Sorcery", "", "AKH", 218, 65270)
Spring = Card("spring", "Spring", ['2', 'G'], ['G', 'U'], "Sorcery", "", "AKH", 219, 65273)
Mind = Card("mind", "Mind", ['4', 'U', 'U'], ['G', 'U'], "Instant", "", "AKH", 219, 65276)
Prepare = Card("prepare", "Prepare", ['1', 'W'], ['W', 'G'], "Instant", "", "AKH", 220, 65279)
Fight = Card("fight", "Fight", ['3', 'G'], ['W', 'G'], "Sorcery", "", "AKH", 220, 65282)
Failure = Card("failure", "Failure", ['1', 'U'], ['U', 'W'], "Instant", "", "AKH", 221, 65285)
Comply = Card("comply", "Comply", ['W'], ['U', 'W'], "Sorcery", "", "AKH", 221, 65288)
Rags = Card("rags", "Rags", ['2', 'B', 'B'], ['U', 'B'], "Sorcery", "", "AKH", 222, 65291)
Riches = Card("riches", "Riches", ['5', 'U', 'U'], ['U', 'B'], "Sorcery", "", "AKH", 222, 65294)
Cut = Card("cut", "Cut", ['1', 'R'], ['B', 'R'], "Sorcery", "", "AKH", 223, 65297)
Ribbons = Card("ribbons", "Ribbons", ['X', 'B', 'B'], ['B', 'R'], "Sorcery", "", "AKH", 223, 65300)
Heaven = Card("heaven", "Heaven", ['X', 'G'], ['G', 'R'], "Instant", "", "AKH", 224, 65303)
Earth = Card("earth", "Earth", ['X', 'R', 'R'], ['G', 'R'], "Sorcery", "", "AKH", 224, 65306)
BontusMonument = Card("bontus_monument", "Bontu's Monument", ['3'], [], "Legendary Artifact", "", "AKH", 225, 65309)
EdificeofAuthority = Card("edifice_of_authority", "Edifice of Authority", ['3'], [], "Artifact", "", "AKH", 226, 65311)
EmbalmersTools = Card("embalmers_tools", "Embalmer's Tools", ['2'], [], "Artifact", "", "AKH", 227, 65313)
GatetotheAfterlife = Card("gate_to_the_afterlife", "Gate to the Afterlife", ['3'], [], "Artifact", "", "AKH", 228, 65315)
HazoretsMonument = Card("hazorets_monument", "Hazoret's Monument", ['3'], [], "Legendary Artifact", "", "AKH", 229, 65317)
HonedKhopesh = Card("honed_khopesh", "Honed Khopesh", ['1'], [], "Artifact", "Equipment", "AKH", 230, 65319)
KefnetsMonument = Card("kefnets_monument", "Kefnet's Monument", ['3'], [], "Legendary Artifact", "", "AKH", 231, 65321)
LuxaRiverShrine = Card("luxa_river_shrine", "Luxa River Shrine", ['3'], [], "Artifact", "", "AKH", 232, 65323)
OketrasMonument = Card("oketras_monument", "Oketra's Monument", ['3'], [], "Legendary Artifact", "", "AKH", 233, 65325)
OraclesVault = Card("oracles_vault", "Oracle's Vault", ['4'], [], "Artifact", "", "AKH", 234, 65327)
PyramidofthePantheon = Card("pyramid_of_the_pantheon", "Pyramid of the Pantheon", ['1'], [], "Artifact", "", "AKH", 235, 65329)
RhonassMonument = Card("rhonass_monument", "Rhonas's Monument", ['3'], [], "Legendary Artifact", "", "AKH", 236, 65331)
ThroneoftheGodPharaoh = Card("throne_of_the_godpharaoh", "Throne of the God-Pharaoh", ['2'], [], "Legendary Artifact", "", "AKH", 237, 65333)
WatchersoftheDead = Card("watchers_of_the_dead", "Watchers of the Dead", ['2'], [], "Artifact Creature", "Cat", "AKH", 238, 65335)
CanyonSlough = Card("canyon_slough", "Canyon Slough", [], ['B', 'R'], "Land", "Swamp Mountain", "AKH", 239, 65337)
# start mixup
CradleoftheAccursed = Card("cradle_of_the_accursed", "Cradle of the Accursed", [], [], "Land", "Desert", "AKH", 241, 65339)
CascadingCataracts = Card("cascading_cataracts", "Cascading Cataracts", [], [], "Land", "", "AKH", 240, 65431)


EvolvingWilds = Card("evolving_wilds", "Evolving Wilds", [], [], "Land", "", "AKH", 242, 65341)
FetidPools = Card("fetid_pools", "Fetid Pools", [], ['U', 'B'], "Land", "Island Swamp", "AKH", 243, 65343)
GraspingDunes = Card("grasping_dunes", "Grasping Dunes", [], [], "Land", "Desert", "AKH", 244, 65345)
IrrigatedFarmland = Card("irrigated_farmland", "Irrigated Farmland", [], ['W', 'U'], "Land", "Plains Island", "AKH", 245, 65347)
# end mixup
PaintedBluffs = Card("painted_bluffs", "Painted Bluffs", [], [], "Land", "Desert", "AKH", 246, 65351)
ScatteredGroves = Card("scattered_groves", "Scattered Groves", [], ['W', 'G'], "Land", "Forest Plains", "AKH", 247, 65353)
ShelteredThicket = Card("sheltered_thicket", "Sheltered Thicket", [], ['R', 'G'], "Land", "Mountain Forest", "AKH", 248, 65355)
SunscorchedDesert = Card("sunscorched_desert", "Sunscorched Desert", [], [], "Land", "Desert", "AKH", 249, 65357)

Plains = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "AKH", 250, 65359)
Plains2 = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "AKH", 252, 65363)
Plains3 = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "AKH", 253, 65365)
Island = Card("island", "Island", [], ['U'], "Basic Land", "Island", "AKH", 251, 65361)
Island2 = Card("island", "Island", [], ['U'], "Basic Land", "Island", "AKH", 255, 65369)
Island3 = Card("island", "Island", [], ['U'], "Basic Land", "Island", "AKH", 256, 65371)
Island4 = Card("island", "Island", [], ['U'], "Basic Land", "Island", "AKH", 257, 65373)
Island5 = Card("island", "Island", [], ['U'], "Basic Land", "Island", "AKH", 259, 65377)
Swamp2 = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "AKH", 261, 65381)
Swamp3 = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "AKH", 262, 65383)
Swamp4 = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "AKH", 260, 65379)
Swamp5 = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "AKH", 258, 65375)
Mountain2 = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "AKH", 264, 65387)
Mountain3 = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "AKH", 265, 65389)
Mountain4 = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "AKH", 266, 65391)
Mountain5 = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "AKH", 263, 65385)
Forest = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "AKH", 254, 65367)
Forest2 = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "AKH", 267, 65393)
Forest3 = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "AKH", 268, 65395)
Forest4 = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "AKH", 269, 65397)

# start mixup
GideonMartialParagon = Card("gideon_martial_paragon", "Gideon, Martial Paragon", ['4', 'W'], ['W'], "Legendary Planeswalker", "Gideon", "AKH", 270, 65443)
CompanionoftheTrials = Card("companion_of_the_trials", "Companion of the Trials", ['2', 'W'], ['W'], "Creature", "Bird Soldier", "AKH", 271, 65445)
GideonsResolve = Card("gideons_resolve", "Gideon's Resolve", ['4', 'W'], ['W'], "Enchantment", "", "AKH", 272, 65447)
GracefulCat = Card("graceful_cat", "Graceful Cat", ['2', 'W'], ['W'], "Creature", "Cat", "AKH", 273, 65449)
StoneQuarry = Card("stone_quarry", "Stone Quarry", [], ['R', 'W'], "Land", "", "AKH", 274, 65451)
LilianaDeathWielder = Card("liliana_death_wielder", "Liliana, Death Wielder", ['5', 'B', 'B'], ['B'], "Legendary Planeswalker", "Liliana", "AKH", 275, 65453)
DesiccatedNaga = Card("desiccated_naga", "Desiccated Naga", ['2', 'B'], ['B'], "Creature", "Zombie Naga", "AKH", 276, 65455)
LilianasInfluence = Card("lilianas_influence", "Liliana's Influence", ['4', 'B', 'B'], ['B'], "Sorcery", "", "AKH", 277, 65457)
TatteredMummy = Card("tattered_mummy", "Tattered Mummy", ['1', 'B'], ['B'], "Creature", "Zombie Jackal", "AKH", 278, 65459)
# end mixup
# wtf
# end wtf
FoulOrchardAKH = Card("foul_orchard", "Foul Orchard", [], ['B', 'G'], "Land", "", "AKH", 279, 65461)
CinderBarrensAKH = Card("cinder_barrens", "Cinder Barrens", [], ['B', 'R'], "Land", "", "AKH", 280, 65463)
ForsakenSanctuaryAKH = Card("forsaken_sanctuary", "Forsaken Sanctuary", [], ['W', 'B'], "Land", "", "AKH", 281, 65465)
HighlandLakeAKH = Card("highland_lake", "Highland Lake", [], ['U', 'R'], "Land", "", "AKH", 282, 65467)
MeanderingRiverAKH = Card("meandering_river", "Meandering River", [], ['W', 'U'], "Land", "", "AKH", 283, 65469)
SubmergedBoneyardAKH = Card("submerged_boneyard", "Submerged Boneyard", [], ['U', 'B'], "Land", "", "AKH", 284, 65471)
TimberGorgeAKH = Card("timber_gorge", "Timber Gorge", [], ['R', 'G'], "Land", "", "AKH", 285, 65473)
TranquilExpanseAKH = Card("tranquil_expanse", "Tranquil Expanse", [], ['G', 'W'], "Land", "", "AKH", 286, 65475)
WoodlandStreamAKH = Card("woodland_stream", "Woodland Stream", [], ['G', 'U'], "Land", "", "AKH", 287, 65477)


# WoodlandStream = Card("woodland_stream", "Woodland Stream", [], ['G', 'U'], "Land", "", "AKH", 287, 65433)

clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
Amonkhet = Set("amonkhet", cards=clsmembers)

