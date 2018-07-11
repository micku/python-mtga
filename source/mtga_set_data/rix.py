
import sys
from .models.card import Card
from .models.card_set import Set
import inspect


BafflingEnd = Card("baffling_end", "Baffling End", ['1', 'W'], ['W'], "Enchantment", "", "RIX", 1, 66619)
BishopofBinding = Card("bishop_of_binding", "Bishop of Binding", ['3', 'W'], ['W'], "Creature", "Vampire Cleric", "RIX", 2, 66621)
BlazingHope = Card("blazing_hope", "Blazing Hope", ['W'], ['W'], "Instant", "", "RIX", 3, 66623)
CleansingRay = Card("cleansing_ray", "Cleansing Ray", ['1', 'W'], ['W'], "Sorcery", "", "RIX", 4, 66625)
DivineVerdict = Card("divine_verdict", "Divine Verdict", ['3', 'W'], ['W'], "Instant", "", "RIX", 5, 66627)
EverdawnChampion = Card("everdawn_champion", "Everdawn Champion", ['1', 'W', 'W'], ['W'], "Creature", "Human Soldier", "RIX", 6, 66629)
ExultantSkymarcher = Card("exultant_skymarcher", "Exultant Skymarcher", ['1', 'W', 'W'], ['W'], "Creature", "Vampire Soldier", "RIX", 7, 66631)
FamishedPaladin = Card("famished_paladin", "Famished Paladin", ['1', 'W'], ['W'], "Creature", "Vampire Knight", "RIX", 8, 66633)
ForerunneroftheLegion = Card("forerunner_of_the_legion", "Forerunner of the Legion", ['2', 'W'], ['W'], "Creature", "Vampire Knight", "RIX", 9, 66635)
ImperialCeratops = Card("imperial_ceratops", "Imperial Ceratops", ['4', 'W'], ['W'], "Creature", "Dinosaur", "RIX", 10, 66637)
LegionConquistador = Card("legion_conquistador", "Legion Conquistador", ['2', 'W'], ['W'], "Creature", "Vampire Soldier", "RIX", 11, 66639)
LuminousBonds = Card("luminous_bonds", "Luminous Bonds", ['2', 'W'], ['W'], "Enchantment", "Aura", "RIX", 12, 66641)
MajesticHeliopterus = Card("majestic_heliopterus", "Majestic Heliopterus", ['3', 'W'], ['W'], "Creature", "Dinosaur", "RIX", 13, 66643)
MartyrofDusk = Card("martyr_of_dusk", "Martyr of Dusk", ['1', 'W'], ['W'], "Creature", "Vampire Soldier", "RIX", 14, 66645)
MomentofTriumph = Card("moment_of_triumph", "Moment of Triumph", ['W'], ['W'], "Instant", "", "RIX", 15, 66647)
PaladinofAtonement = Card("paladin_of_atonement", "Paladin of Atonement", ['1', 'W'], ['W'], "Creature", "Vampire Knight", "RIX", 16, 66649)
PrideofConquerors = Card("pride_of_conquerors", "Pride of Conquerors", ['1', 'W'], ['W'], "Instant", "", "RIX", 17, 66651)
RadiantDestiny = Card("radiant_destiny", "Radiant Destiny", ['2', 'W'], ['W'], "Enchantment", "", "RIX", 18, 66653)
RaptorCompanion = Card("raptor_companion", "Raptor Companion", ['1', 'W'], ['W'], "Creature", "Dinosaur", "RIX", 19, 66655)
SanguineGlorifier = Card("sanguine_glorifier", "Sanguine Glorifier", ['3', 'W'], ['W'], "Creature", "Vampire Cleric", "RIX", 20, 66657)
SkymarcherAspirant = Card("skymarcher_aspirant", "Skymarcher Aspirant", ['W'], ['W'], "Creature", "Vampire Soldier", "RIX", 21, 66659)
SlaughtertheStrong = Card("slaughter_the_strong", "Slaughter the Strong", ['1', 'W', 'W'], ['W'], "Sorcery", "", "RIX", 22, 66661)
SnubhornSentry = Card("snubhorn_sentry", "Snubhorn Sentry", ['W'], ['W'], "Creature", "Dinosaur", "RIX", 23, 66663)
SphinxsDecree = Card("sphinxs_decree", "Sphinx's Decree", ['1', 'W'], ['W'], "Sorcery", "", "RIX", 24, 66665)
SquiresDevotion = Card("squires_devotion", "Squire's Devotion", ['2', 'W'], ['W'], "Enchantment", "Aura", "RIX", 25, 66667)
SunSentinel = Card("sun_sentinel", "Sun Sentinel", ['1', 'W'], ['W'], "Creature", "Human Soldier", "RIX", 26, 66669)
SunCrestedPterodon = Card("suncrested_pterodon", "Sun-Crested Pterodon", ['4', 'W'], ['W'], "Creature", "Dinosaur", "RIX", 27, 66671)
TempleAltisaur = Card("temple_altisaur", "Temple Altisaur", ['4', 'W'], ['W'], "Creature", "Dinosaur", "RIX", 28, 66673)
TrapjawTyrant = Card("trapjaw_tyrant", "Trapjaw Tyrant", ['3', 'W', 'W'], ['W'], "Creature", "Dinosaur", "RIX", 29, 66675)
ZetalpaPrimalDawn = Card("zetalpa_primal_dawn", "Zetalpa, Primal Dawn", ['6', 'W', 'W'], ['W'], "Legendary Creature", "Elder Dinosaur", "RIX", 30, 66677)
AdmiralsOrder = Card("admirals_order", "Admiral's Order", ['1', 'U', 'U'], ['U'], "Instant", "", "RIX", 31, 66679)
AquaticIncursion = Card("aquatic_incursion", "Aquatic Incursion", ['3', 'U'], ['U'], "Enchantment", "", "RIX", 32, 66681)
CraftyCutpurse = Card("crafty_cutpurse", "Crafty Cutpurse", ['3', 'U'], ['U'], "Creature", "Human Pirate", "RIX", 33, 66683)
CrashingTide = Card("crashing_tide", "Crashing Tide", ['2', 'U'], ['U'], "Sorcery", "", "RIX", 34, 66685)
CuriousObsession = Card("curious_obsession", "Curious Obsession", ['U'], ['U'], "Enchantment", "Aura", "RIX", 35, 66687)
DeadeyeRigHauler = Card("deadeye_righauler", "Deadeye Rig-Hauler", ['3', 'U'], ['U'], "Creature", "Human Pirate", "RIX", 36, 66689)
ExpelfromOrazca = Card("expel_from_orazca", "Expel from Orazca", ['1', 'U'], ['U'], "Instant", "", "RIX", 37, 66691)
FloodofRecollection = Card("flood_of_recollection", "Flood of Recollection", ['U', 'U'], ['U'], "Sorcery", "", "RIX", 38, 66693)
Hornswoggle = Card("hornswoggle", "Hornswoggle", ['2', 'U'], ['U'], "Instant", "", "RIX", 39, 66695)
InducedAmnesia = Card("induced_amnesia", "Induced Amnesia", ['2', 'U'], ['U'], "Enchantment", "", "RIX", 40, 66697)
KitesailCorsair = Card("kitesail_corsair", "Kitesail Corsair", ['1', 'U'], ['U'], "Creature", "Human Pirate", "RIX", 41, 66699)
KumenasAwakening = Card("kumenas_awakening", "Kumena's Awakening", ['2', 'U', 'U'], ['U'], "Enchantment", "", "RIX", 42, 66701)
MistCloakedHerald = Card("mistcloaked_herald", "Mist-Cloaked Herald", ['U'], ['U'], "Creature", "Merfolk Warrior", "RIX", 43, 66703)
Negate = Card("negate", "Negate", ['1', 'U'], ['U'], "Instant", "", "RIX", 44, 66705)
NezahalPrimalTide = Card("nezahal_primal_tide", "Nezahal, Primal Tide", ['5', 'U', 'U'], ['U'], "Legendary Creature", "Elder Dinosaur", "RIX", 45, 66707)
ReleasetotheWind = Card("release_to_the_wind", "Release to the Wind", ['2', 'U'], ['U'], "Instant", "", "RIX", 46, 66709)
RiverDarter = Card("river_darter", "River Darter", ['2', 'U'], ['U'], "Creature", "Merfolk Warrior", "RIX", 47, 66711)
RiverwiseAugur = Card("riverwise_augur", "Riverwise Augur", ['3', 'U'], ['U'], "Creature", "Merfolk Wizard", "RIX", 48, 66713)
SailorofMeans = Card("sailor_of_means", "Sailor of Means", ['2', 'U'], ['U'], "Creature", "Human Pirate", "RIX", 49, 66715)
SeaLegs = Card("sea_legs", "Sea Legs", ['U'], ['U'], "Enchantment", "Aura", "RIX", 50, 66717)
SeafloorOracle = Card("seafloor_oracle", "Seafloor Oracle", ['2', 'U', 'U'], ['U'], "Creature", "Merfolk Wizard", "RIX", 51, 66719)
SecretsoftheGoldenCity = Card("secrets_of_the_golden_city", "Secrets of the Golden City", ['1', 'U', 'U'], ['U'], "Sorcery", "", "RIX", 52, 66721)
SilvergillAdept = Card("silvergill_adept", "Silvergill Adept", ['1', 'U'], ['U'], "Creature", "Merfolk Wizard", "RIX", 53, 66723)
SirenReaver = Card("siren_reaver", "Siren Reaver", ['3', 'U'], ['U'], "Creature", "Siren Pirate", "RIX", 54, 66725)
SlipperyScoundrel = Card("slippery_scoundrel", "Slippery Scoundrel", ['2', 'U'], ['U'], "Creature", "Human Pirate", "RIX", 55, 66727)
SouloftheRapids = Card("soul_of_the_rapids", "Soul of the Rapids", ['3', 'U', 'U'], ['U'], "Creature", "Elemental", "RIX", 56, 66729)
SpireWinder = Card("spire_winder", "Spire Winder", ['3', 'U'], ['U'], "Creature", "Snake", "RIX", 57, 66731)
SwornGuardian = Card("sworn_guardian", "Sworn Guardian", ['1', 'U'], ['U'], "Creature", "Merfolk Warrior", "RIX", 58, 66733)
TimestreamNavigator = Card("timestream_navigator", "Timestream Navigator", ['1', 'U'], ['U'], "Creature", "Human Pirate Wizard", "RIX", 59, 66735)
WarkiteMarauder = Card("warkite_marauder", "Warkite Marauder", ['1', 'U'], ['U'], "Creature", "Human Pirate", "RIX", 60, 66737)
Waterknot = Card("waterknot", "Waterknot", ['1', 'U', 'U'], ['U'], "Enchantment", "Aura", "RIX", 61, 66739)
ArterialFlow = Card("arterial_flow", "Arterial Flow", ['1', 'B', 'B'], ['B'], "Sorcery", "", "RIX", 62, 66741)
CanalMonitor = Card("canal_monitor", "Canal Monitor", ['4', 'B'], ['B'], "Creature", "Lizard", "RIX", 63, 66743)
ChampionofDusk = Card("champion_of_dusk", "Champion of Dusk", ['3', 'B', 'B'], ['B'], "Creature", "Vampire Knight", "RIX", 64, 66745)
DarkInquiry = Card("dark_inquiry", "Dark Inquiry", ['2', 'B'], ['B'], "Sorcery", "", "RIX", 65, 66747)
DeadMansChest = Card("dead_mans_chest", "Dead Man's Chest", ['1', 'B'], ['B'], "Enchantment", "Aura", "RIX", 66, 66749)
DinosaurHunter = Card("dinosaur_hunter", "Dinosaur Hunter", ['1', 'B'], ['B'], "Creature", "Human Pirate", "RIX", 67, 66751)
DireFleetPoisoner = Card("dire_fleet_poisoner", "Dire Fleet Poisoner", ['1', 'B'], ['B'], "Creature", "Human Pirate", "RIX", 68, 66753)
DuskCharger = Card("dusk_charger", "Dusk Charger", ['3', 'B'], ['B'], "Creature", "Horse", "RIX", 69, 66755)
DuskLegionZealot = Card("dusk_legion_zealot", "Dusk Legion Zealot", ['1', 'B'], ['B'], "Creature", "Vampire Soldier", "RIX", 70, 66757)
FathomFleetBoarder = Card("fathom_fleet_boarder", "Fathom Fleet Boarder", ['2', 'B'], ['B'], "Creature", "Orc Pirate", "RIX", 71, 66759)
ForerunneroftheCoalition = Card("forerunner_of_the_coalition", "Forerunner of the Coalition", ['2', 'B'], ['B'], "Creature", "Human Pirate", "RIX", 72, 66761)
GoldenDemise = Card("golden_demise", "Golden Demise", ['1', 'B', 'B'], ['B'], "Sorcery", "", "RIX", 73, 66763)
GraspingScoundrel = Card("grasping_scoundrel", "Grasping Scoundrel", ['B'], ['B'], "Creature", "Human Pirate", "RIX", 74, 66765)
GruesomeFate = Card("gruesome_fate", "Gruesome Fate", ['2', 'B'], ['B'], "Sorcery", "", "RIX", 75, 66767)
Impale = Card("impale", "Impale", ['2', 'B', 'B'], ['B'], "Sorcery", "", "RIX", 76, 66769)
MastermindsAcquisition = Card("masterminds_acquisition", "Mastermind's Acquisition", ['2', 'B', 'B'], ['B'], "Sorcery", "", "RIX", 77, 66771)
MausoleumHarpy = Card("mausoleum_harpy", "Mausoleum Harpy", ['4', 'B'], ['B'], "Creature", "Harpy", "RIX", 78, 66773)
MomentofCraving = Card("moment_of_craving", "Moment of Craving", ['1', 'B'], ['B'], "Instant", "", "RIX", 79, 66775)
OathswornVampire = Card("oathsworn_vampire", "Oathsworn Vampire", ['1', 'B'], ['B'], "Creature", "Vampire Knight", "RIX", 80, 66777)
PitilessPlunderer = Card("pitiless_plunderer", "Pitiless Plunderer", ['3', 'B'], ['B'], "Creature", "Human Pirate", "RIX", 81, 66779)
RavenousChupacabra = Card("ravenous_chupacabra", "Ravenous Chupacabra", ['2', 'B', 'B'], ['B'], "Creature", "Beast Horror", "RIX", 82, 66781)
ReaverAmbush = Card("reaver_ambush", "Reaver Ambush", ['2', 'B'], ['B'], "Instant", "", "RIX", 83, 66783)
Recover = Card("recover", "Recover", ['2', 'B'], ['B'], "Sorcery", "", "RIX", 84, 66785)
SadisticSkymarcher = Card("sadistic_skymarcher", "Sadistic Skymarcher", ['2', 'B'], ['B'], "Creature", "Vampire Soldier", "RIX", 85, 66787)
TetzimocPrimalDeath = Card("tetzimoc_primal_death", "Tetzimoc, Primal Death", ['4', 'B', 'B'], ['B'], "Legendary Creature", "Elder Dinosaur", "RIX", 86, 66789)
TombRobber = Card("tomb_robber", "Tomb Robber", ['2', 'B'], ['B'], "Creature", "Human Pirate", "RIX", 87, 66791)
TwilightProphet = Card("twilight_prophet", "Twilight Prophet", ['2', 'B', 'B'], ['B'], "Creature", "Vampire Cleric", "RIX", 88, 66793)
VampireRevenant = Card("vampire_revenant", "Vampire Revenant", ['3', 'B'], ['B'], "Creature", "Vampire Spirit", "RIX", 89, 66795)
VonasHunger = Card("vonas_hunger", "Vona's Hunger", ['2', 'B'], ['B'], "Instant", "", "RIX", 90, 66797)
VoraciousVampire = Card("voracious_vampire", "Voracious Vampire", ['2', 'B'], ['B'], "Creature", "Vampire Knight", "RIX", 91, 66799)
BloodSun = Card("blood_sun", "Blood Sun", ['2', 'R'], ['R'], "Enchantment", "", "RIX", 92, 66801)
Bombard = Card("bombard", "Bombard", ['2', 'R'], ['R'], "Instant", "", "RIX", 93, 66803)
BrasssBounty = Card("brasss_bounty", "Brass's Bounty", ['6', 'R'], ['R'], "Sorcery", "", "RIX", 94, 66805)
BrazenFreebooter = Card("brazen_freebooter", "Brazen Freebooter", ['3', 'R'], ['R'], "Creature", "Human Pirate", "RIX", 95, 66807)
BuccaneersBravado = Card("buccaneers_bravado", "Buccaneer's Bravado", ['1', 'R'], ['R'], "Instant", "", "RIX", 96, 66809)
ChargingTuskodon = Card("charging_tuskodon", "Charging Tuskodon", ['3', 'R', 'R'], ['R'], "Creature", "Dinosaur", "RIX", 97, 66811)
DaringBuccaneer = Card("daring_buccaneer", "Daring Buccaneer", ['R'], ['R'], "Creature", "Human Pirate", "RIX", 98, 66813)
DireFleetDaredevil = Card("dire_fleet_daredevil", "Dire Fleet Daredevil", ['1', 'R'], ['R'], "Creature", "Human Pirate", "RIX", 99, 66815)
EtaliPrimalStorm = Card("etali_primal_storm", "Etali, Primal Storm", ['4', 'R', 'R'], ['R'], "Legendary Creature", "Elder Dinosaur", "RIX", 100, 66817)
FanaticalFirebrand = Card("fanatical_firebrand", "Fanatical Firebrand", ['R'], ['R'], "Creature", "Goblin Pirate", "RIX", 101, 66819)
ForerunneroftheEmpire = Card("forerunner_of_the_empire", "Forerunner of the Empire", ['3', 'R'], ['R'], "Creature", "Human Soldier", "RIX", 102, 66821)
FormoftheDinosaur = Card("form_of_the_dinosaur", "Form of the Dinosaur", ['4', 'R', 'R'], ['R'], "Enchantment", "", "RIX", 103, 66823)
FrilledDeathspitter = Card("frilled_deathspitter", "Frilled Deathspitter", ['2', 'R'], ['R'], "Creature", "Dinosaur", "RIX", 104, 66825)
GoblinTrailblazer = Card("goblin_trailblazer", "Goblin Trailblazer", ['1', 'R'], ['R'], "Creature", "Goblin Pirate", "RIX", 105, 66827)
Mutiny = Card("mutiny", "Mutiny", ['R'], ['R'], "Sorcery", "", "RIX", 106, 66829)
NeedletoothRaptor = Card("needletooth_raptor", "Needletooth Raptor", ['3', 'R'], ['R'], "Creature", "Dinosaur", "RIX", 107, 66831)
OrazcaRaptor = Card("orazca_raptor", "Orazca Raptor", ['2', 'R', 'R'], ['R'], "Creature", "Dinosaur", "RIX", 108, 66833)
PiratesPillage = Card("pirates_pillage", "Pirate's Pillage", ['3', 'R'], ['R'], "Sorcery", "", "RIX", 109, 66835)
RecklessRage = Card("reckless_rage", "Reckless Rage", ['R'], ['R'], "Instant", "", "RIX", 110, 66837)
RekindlingPhoenix = Card("rekindling_phoenix", "Rekindling Phoenix", ['2', 'R', 'R'], ['R'], "Creature", "Phoenix", "RIX", 111, 66839)
SeeRed = Card("see_red", "See Red", ['1', 'R'], ['R'], "Enchantment", "Aura", "RIX", 112, 66841)
ShaketheFoundations = Card("shake_the_foundations", "Shake the Foundations", ['2', 'R'], ['R'], "Instant", "", "RIX", 113, 66843)
Shatter = Card("shatter", "Shatter", ['1', 'R'], ['R'], "Instant", "", "RIX", 114, 66845)
SilvercladFerocidons = Card("silverclad_ferocidons", "Silverclad Ferocidons", ['5', 'R', 'R'], ['R'], "Creature", "Dinosaur", "RIX", 115, 66847)
StampedingHorncrest = Card("stampeding_horncrest", "Stampeding Horncrest", ['4', 'R'], ['R'], "Creature", "Dinosaur", "RIX", 116, 66849)
StormFleetSwashbuckler = Card("storm_fleet_swashbuckler", "Storm Fleet Swashbuckler", ['1', 'R'], ['R'], "Creature", "Human Pirate", "RIX", 117, 66851)
SunCollaredRaptor = Card("suncollared_raptor", "Sun-Collared Raptor", ['1', 'R'], ['R'], "Creature", "Dinosaur", "RIX", 118, 66853)
SwaggeringCorsair = Card("swaggering_corsair", "Swaggering Corsair", ['2', 'R'], ['R'], "Creature", "Human Pirate", "RIX", 119, 66855)
TilonallisCrown = Card("tilonallis_crown", "Tilonalli's Crown", ['1', 'R'], ['R'], "Enchantment", "Aura", "RIX", 120, 66857)
TilonallisSummoner = Card("tilonallis_summoner", "Tilonalli's Summoner", ['1', 'R'], ['R'], "Creature", "Human Shaman", "RIX", 121, 66859)
AggressiveUrge = Card("aggressive_urge", "Aggressive Urge", ['1', 'G'], ['G'], "Instant", "", "RIX", 122, 66861)
Cacophodon = Card("cacophodon", "Cacophodon", ['3', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 123, 66863)
CherishedHatchling = Card("cherished_hatchling", "Cherished Hatchling", ['1', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 124, 66865)
ColossalDreadmaw = Card("colossal_dreadmaw", "Colossal Dreadmaw", ['4', 'G', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 125, 66867)
CrestedHerdcaller = Card("crested_herdcaller", "Crested Herdcaller", ['3', 'G', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 126, 66869)
DeeprootElite = Card("deeproot_elite", "Deeproot Elite", ['1', 'G'], ['G'], "Creature", "Merfolk Warrior", "RIX", 127, 66871)
EntertheUnknown = Card("enter_the_unknown", "Enter the Unknown", ['G'], ['G'], "Sorcery", "", "RIX", 128, 66873)
ForerunneroftheHeralds = Card("forerunner_of_the_heralds", "Forerunner of the Heralds", ['3', 'G'], ['G'], "Creature", "Merfolk Scout", "RIX", 129, 66875)
GhaltaPrimalHunger = Card("ghalta_primal_hunger", "Ghalta, Primal Hunger", ['10', 'G', 'G'], ['G'], "Legendary Creature", "Elder Dinosaur", "RIX", 130, 66877)
GiltgroveStalker = Card("giltgrove_stalker", "Giltgrove Stalker", ['1', 'G'], ['G'], "Creature", "Merfolk Warrior", "RIX", 131, 66879)
HardyVeteran = Card("hardy_veteran", "Hardy Veteran", ['1', 'G'], ['G'], "Creature", "Human Warrior", "RIX", 132, 66881)
HunttheWeak = Card("hunt_the_weak", "Hunt the Weak", ['3', 'G'], ['G'], "Sorcery", "", "RIX", 133, 66883)
JadeBearer = Card("jade_bearer", "Jade Bearer", ['G'], ['G'], "Creature", "Merfolk Shaman", "RIX", 134, 66885)
JadecraftArtisan = Card("jadecraft_artisan", "Jadecraft Artisan", ['3', 'G'], ['G'], "Creature", "Merfolk Shaman", "RIX", 135, 66887)
JadelightRanger = Card("jadelight_ranger", "Jadelight Ranger", ['1', 'G', 'G'], ['G'], "Creature", "Merfolk Scout", "RIX", 136, 66889)
JunglebornPioneer = Card("jungleborn_pioneer", "Jungleborn Pioneer", ['2', 'G'], ['G'], "Creature", "Merfolk Scout", "RIX", 137, 66891)
KnightoftheStampede = Card("knight_of_the_stampede", "Knight of the Stampede", ['3', 'G'], ['G'], "Creature", "Human Knight", "RIX", 138, 66893)
Naturalize = Card("naturalize", "Naturalize", ['1', 'G'], ['G'], "Instant", "", "RIX", 139, 66895)
OrazcaFrillback = Card("orazca_frillback", "Orazca Frillback", ['2', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 140, 66897)
OvergrownArmasaur = Card("overgrown_armasaur", "Overgrown Armasaur", ['3', 'G', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 141, 66899)
PathofDiscovery = Card("path_of_discovery", "Path of Discovery", ['3', 'G'], ['G'], "Enchantment", "", "RIX", 142, 66901)
Plummet = Card("plummet", "Plummet", ['1', 'G'], ['G'], "Instant", "", "RIX", 143, 66903)
Polyraptor = Card("polyraptor", "Polyraptor", ['6', 'G', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 144, 66905)
StrengthofthePack = Card("strength_of_the_pack", "Strength of the Pack", ['4', 'G', 'G'], ['G'], "Sorcery", "", "RIX", 145, 66907)
SwiftWarden = Card("swift_warden", "Swift Warden", ['1', 'G', 'G'], ['G'], "Creature", "Merfolk Warrior", "RIX", 146, 66909)
TendershootDryad = Card("tendershoot_dryad", "Tendershoot Dryad", ['4', 'G'], ['G'], "Creature", "Dryad", "RIX", 147, 66911)
ThrashingBrontodon = Card("thrashing_brontodon", "Thrashing Brontodon", ['1', 'G', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 148, 66913)
ThunderherdMigration = Card("thunderherd_migration", "Thunderherd Migration", ['1', 'G'], ['G'], "Sorcery", "", "RIX", 149, 66915)
WaywardSwordtooth = Card("wayward_swordtooth", "Wayward Swordtooth", ['2', 'G'], ['G'], "Creature", "Dinosaur", "RIX", 150, 66917)
WorldShaper = Card("world_shaper", "World Shaper", ['3', 'G'], ['G'], "Creature", "Merfolk Shaman", "RIX", 151, 66919)
AngraththeFlameChained = Card("angrath_the_flamechained", "Angrath, the Flame-Chained", ['3', 'B', 'R'], ['B', 'R'], "Legendary Planeswalker", "Angrath", "RIX", 152, 66921)
AtzocanSeer = Card("atzocan_seer", "Atzocan Seer", ['1', 'G', 'W'], ['W', 'G'], "Creature", "Human Druid", "RIX", 153, 66923)
AzortheLawbringer = Card("azor_the_lawbringer", "Azor, the Lawbringer", ['2', 'W', 'W', 'U', 'U'], ['W', 'U'], "Legendary Creature", "Sphinx", "RIX", 154, 66925)
DeadeyeBrawler = Card("deadeye_brawler", "Deadeye Brawler", ['2', 'U', 'B'], ['U', 'B'], "Creature", "Human Pirate", "RIX", 155, 66927)
DireFleetNeckbreaker = Card("dire_fleet_neckbreaker", "Dire Fleet Neckbreaker", ['2', 'B', 'R'], ['B', 'R'], "Creature", "Orc Pirate", "RIX", 156, 66929)
ElendatheDuskRose = Card("elenda_the_dusk_rose", "Elenda, the Dusk Rose", ['2', 'W', 'B'], ['W', 'B'], "Legendary Creature", "Vampire Knight", "RIX", 157, 66931)
HadanasClimb = Card("hadanas_climb", "Hadana's Climb", ['1', 'G', 'U'], ['G', 'U'], "Legendary Enchantment", "", "RIX", 158, 66933)
WingedTempleofOrazca = Card("winged_temple_of_orazca", "Winged Temple of Orazca", [], ['G', 'U'], "Legendary Land", "", "RIX", 158, 66935)
HuatliRadiantChampion = Card("huatli_radiant_champion", "Huatli, Radiant Champion", ['2', 'G', 'W'], ['W', 'G'], "Legendary Planeswalker", "Huatli", "RIX", 159, 66937)
JourneytoEternity = Card("journey_to_eternity", "Journey to Eternity", ['1', 'B', 'G'], ['B', 'G'], "Legendary Enchantment", "Aura", "RIX", 160, 66939)
AtzalCaveofEternity = Card("atzal_cave_of_eternity", "Atzal, Cave of Eternity", [], ['B', 'G'], "Legendary Land", "", "RIX", 160, 66941)
JungleCreeper = Card("jungle_creeper", "Jungle Creeper", ['1', 'B', 'G'], ['B', 'G'], "Creature", "Elemental", "RIX", 161, 66943)
KumenaTyrantofOrazca = Card("kumena_tyrant_of_orazca", "Kumena, Tyrant of Orazca", ['1', 'G', 'U'], ['U', 'G'], "Legendary Creature", "Merfolk Shaman", "RIX", 162, 66945)
LegionLieutenant = Card("legion_lieutenant", "Legion Lieutenant", ['W', 'B'], ['W', 'B'], "Creature", "Vampire Knight", "RIX", 163, 66947)
MerfolkMistbinder = Card("merfolk_mistbinder", "Merfolk Mistbinder", ['G', 'U'], ['U', 'G'], "Creature", "Merfolk Shaman", "RIX", 164, 66949)
PathofMettle = Card("path_of_mettle", "Path of Mettle", ['R', 'W'], ['W', 'R'], "Legendary Enchantment", "", "RIX", 165, 66951)
MetzaliTowerofTriumph = Card("metzali_tower_of_triumph", "Metzali, Tower of Triumph", [], ['W', 'R'], "Legendary Land", "", "RIX", 165, 66953)
ProfaneProcession = Card("profane_procession", "Profane Procession", ['1', 'W', 'B'], ['W', 'B'], "Legendary Enchantment", "", "RIX", 166, 66955)
TomboftheDuskRose = Card("tomb_of_the_dusk_rose", "Tomb of the Dusk Rose", [], ['W', 'B'], "Legendary Land", "", "RIX", 166, 66957)
ProteanRaider = Card("protean_raider", "Protean Raider", ['1', 'U', 'R'], ['U', 'R'], "Creature", "Shapeshifter Pirate", "RIX", 167, 66959)
RagingRegisaur = Card("raging_regisaur", "Raging Regisaur", ['2', 'R', 'G'], ['R', 'G'], "Creature", "Dinosaur", "RIX", 168, 66961)
RelentlessRaptor = Card("relentless_raptor", "Relentless Raptor", ['R', 'W'], ['W', 'R'], "Creature", "Dinosaur", "RIX", 169, 66963)
ResplendentGriffin = Card("resplendent_griffin", "Resplendent Griffin", ['1', 'W', 'U'], ['W', 'U'], "Creature", "Griffin", "RIX", 170, 66965)
SiegehornCeratops = Card("siegehorn_ceratops", "Siegehorn Ceratops", ['G', 'W'], ['W', 'G'], "Creature", "Dinosaur", "RIX", 171, 66967)
StormFleetSprinter = Card("storm_fleet_sprinter", "Storm Fleet Sprinter", ['1', 'U', 'R'], ['U', 'R'], "Creature", "Human Pirate", "RIX", 172, 66969)
StormtheVault = Card("storm_the_vault", "Storm the Vault", ['2', 'U', 'R'], ['U', 'R'], "Legendary Enchantment", "", "RIX", 173, 66971)
VaultofCatlacan = Card("vault_of_catlacan", "Vault of Catlacan", [], ['U', 'R'], "Legendary Land", "", "RIX", 173, 66973)
ZacamaPrimalCalamity = Card("zacama_primal_calamity", "Zacama, Primal Calamity", ['6', 'R', 'G', 'W'], ['W', 'R', 'G'], "Legendary Creature", "Elder Dinosaur", "RIX", 174, 66975)
AwakenedAmalgam = Card("awakened_amalgam", "Awakened Amalgam", ['4'], [], "Artifact Creature", "Golem", "RIX", 175, 66977)
AzorsGateway = Card("azors_gateway", "Azor's Gateway", ['2'], [], "Legendary Artifact", "", "RIX", 176, 66979)
SanctumoftheSun = Card("sanctum_of_the_sun", "Sanctum of the Sun", [], [], "Legendary Land", "", "RIX", 176, 66981)
CaptainsHook = Card("captains_hook", "Captain's Hook", ['3'], [], "Artifact", "Equipment", "RIX", 177, 66983)
GleamingBarrier = Card("gleaming_barrier", "Gleaming Barrier", ['2'], [], "Artifact Creature", "Wall", "RIX", 178, 66985)
GoldenGuardian = Card("golden_guardian", "Golden Guardian", ['4'], [], "Artifact Creature", "Golem", "RIX", 179, 66987)
GoldForgeGarrison = Card("goldforge_garrison", "Gold-Forge Garrison", [], [], "Land", "", "RIX", 179, 66989)
TheImmortalSun = Card("the_immortal_sun", "The Immortal Sun", ['6'], [], "Legendary Artifact", "", "RIX", 180, 66991)
OrazcaRelic = Card("orazca_relic", "Orazca Relic", ['3'], [], "Artifact", "", "RIX", 181, 66993)
SilentGravestone = Card("silent_gravestone", "Silent Gravestone", ['1'], [], "Artifact", "", "RIX", 182, 66995)
StriderHarness = Card("strider_harness", "Strider Harness", ['3'], [], "Artifact", "Equipment", "RIX", 183, 66997)
TravelersAmulet = Card("travelers_amulet", "Traveler's Amulet", ['1'], [], "Artifact", "", "RIX", 184, 66999)
ArchofOrazca = Card("arch_of_orazca", "Arch of Orazca", [], [], "Land", "", "RIX", 185, 67001)
EvolvingWilds = Card("evolving_wilds", "Evolving Wilds", [], [], "Land", "", "RIX", 186, 67003)
ForsakenSanctuary = Card("forsaken_sanctuary", "Forsaken Sanctuary", [], ['W', 'B'], "Land", "", "RIX", 187, 67005)
FoulOrchard = Card("foul_orchard", "Foul Orchard", [], ['B', 'G'], "Land", "", "RIX", 188, 67007)
HighlandLake = Card("highland_lake", "Highland Lake", [], ['U', 'R'], "Land", "", "RIX", 189, 67009)
StoneQuarry = Card("stone_quarry", "Stone Quarry", [], ['R', 'W'], "Land", "", "RIX", 190, 67011)
WoodlandStream = Card("woodland_stream", "Woodland Stream", [], ['G', 'U'], "Land", "", "RIX", 191, 67013)
Plains = Card("plains", "Plains", [], ['W'], "Basic Land", "Plains", "RIX", 192, 67015)
Island = Card("island", "Island", [], ['U'], "Basic Land", "Island", "RIX", 193, 67017)
Swamp = Card("swamp", "Swamp", [], ['B'], "Basic Land", "Swamp", "RIX", 194, 67019)
Mountain = Card("mountain", "Mountain", [], ['R'], "Basic Land", "Mountain", "RIX", 195, 67021)
Forest = Card("forest", "Forest", [], ['G'], "Basic Land", "Forest", "RIX", 196, 67023)
VraskaSchemingGorgon = Card("vraska_scheming_gorgon", "Vraska, Scheming Gorgon", ['4', 'B', 'B'], ['B'], "Legendary Planeswalker", "Vraska", "RIX", 197, 67025)
VampireChampion = Card("vampire_champion", "Vampire Champion", ['3', 'B'], ['B'], "Creature", "Vampire Soldier", "RIX", 198, 67027)
VraskasConquistador = Card("vraskas_conquistador", "Vraska's Conquistador", ['1', 'B'], ['B'], "Creature", "Vampire Soldier", "RIX", 199, 67029)
VraskasScorn = Card("vraskas_scorn", "Vraska's Scorn", ['2', 'B', 'B'], ['B'], "Sorcery", "", "RIX", 200, 67031)
AngrathMinotaurPirate = Card("angrath_minotaur_pirate", "Angrath, Minotaur Pirate", ['4', 'B', 'R'], ['B', 'R'], "Legendary Planeswalker", "Angrath", "RIX", 201, 67033)
AngrathsAmbusher = Card("angraths_ambusher", "Angrath's Ambusher", ['2', 'B'], ['B'], "Creature", "Orc Pirate", "RIX", 202, 67035)
SwabGoblin = Card("swab_goblin", "Swab Goblin", ['1', 'R'], ['R'], "Creature", "Goblin Pirate", "RIX", 203, 67037)
AngrathsFury = Card("angraths_fury", "Angrath's Fury", ['3', 'B', 'R'], ['B', 'R'], "Sorcery", "", "RIX", 204, 67039)
CinderBarrens = Card("cinder_barrens", "Cinder Barrens", [], ['B', 'R'], "Land", "", "RIX", 205, 67041)

clsmembers = [card for name, card in inspect.getmembers(sys.modules[__name__]) if isinstance(card, Card)]
RivalsOfIxalan = Set("rivals_of_ixalan", cards=clsmembers)

