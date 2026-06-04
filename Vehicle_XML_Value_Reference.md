# Farming Simulator 25 — Vehicle XML Complete Value Reference

> Companion to `shared/xml/documentation/vehicle.html`. That file lists every valid **tag** and **attribute** for a vehicle XML, but for many attributes it only shows the *default* value (e.g. it documents `attacherJoint#jointType` as `Type: String, Default: implement` and never reveals the other 21 joint types). This document fills that gap: the **complete set of valid values** for every enumerated/registry-backed vehicle-XML key, extracted directly from the game's schema, data files, and decompiled Lua.

**Game version:** 1.19.0.0 (descVersion 109)  
**Generated from:**
- `shared/xml/schema/vehicle.xsd` — schema-carried `xs:enumeration` value sets
- `data/maps/maps_*.xml`, `data/shared/**`, `dataS/*.xml` — registry data files
- `dataS/scripts/**` — decompiled Lua registration calls
- `ClaudeDir/dlcs/*` — unpacked DLC packs (additions labeled per pack)

**Two kinds of values:**
1. **Schema-defined enums (Part 1)** — the XSD itself constrains the value to a fixed list. The HTML *sometimes* shows these inline and sometimes doesn't.
2. **Registry-backed strings (Part 2)** — the XSD types the attribute as a free `g_string`, but the game only accepts values that were registered in a data file or Lua at load time. **This is the `jointType` problem.** These sets are *extensible*: maps, DLCs, and mods can register more at runtime, so the lists below are the **base-game + unpacked-DLC** baseline.

---

## Part 1 — Schema-defined enums (from `vehicle.xsd`)

146 enum-constrained attribute locations across the vehicle XML, collapsing to the distinct value-sets below. Each block lists the attribute(s) that use the set, the default (if any), and the full value list.

### `#type`  (23 values)
**Used at 70 location(s):** `attachSound.loopSynthesisLoad.modifier`; `attachSound.loopSynthesisRpm.modifier`; `attachSound.lowpassGain.modifier`; `attachSound.pitch.modifier`; `attachSound.volume.modifier`; `detachSound.loopSynthesisLoad.modifier` …

```
ACCELERATE, BLOW_OFF_VALVE_STATE, BOATYARD_LAUNCHING_SPEED, BOATYARD_MOVING_SPEED, BRAKE_TIME, CARRIAGE_SPEED,
COMBINE_LOAD, CRUISECONTROL, DECELERATE, DIFFERENTIAL_SPEED, DRIVING_DIRECTION, FOOTBALL_SPEED,
MOTOR_LOAD, MOTOR_RPM, MOTOR_RPM_REAL, MOWER_LOAD, ROLLERCOASTER_CURVE, ROLLERCOASTER_SPEED,
SPEED, SUSPENSION, TURNED_ON_SPEED, WHEEL_SUSPENSION, WIND_TURBINE_LOAD
```

### `#valueType`  (23 values)
**Used at 1 location(s):** `vehicle.motorized.dashboards.dashboard`

```
battery, clutchPedal, directionBackward, directionForward, directionForwardExclusive, directionNeutral,
fuelUsage, gear, gearGroup, gearGroupIndex, gearIndex, gearShiftDown,
gearShiftUp, gearShiftUpDown, ignitionState, load, motorTemperature, motorTemperatureWarning,
movingDirection, movingDirectionLetter, rpm, speed, speedDir
```

### `#name`  (16 values)
**Used at 2 location(s):** `vehicle.lights.sharedLight.function`; `vehicle.lights.staticLightCompounds.staticLightCompound.function`

```
BACK_BRAKE_LIGHT, BACK_LIGHT, BOTTOM_LIGHT, BRAKE_LIGHT, DAY_TIME_RUNNING_LIGHT, DEFAULT_LIGHT,
DEFAULT_LIGHT_HIGH_BEAM, HIGH_BEAM, REVERSE_LIGHT, TOP_LIGHT, TURN_LIGHT_LEFT, TURN_LIGHT_RIGHT,
WORK_LIGHT_ADDITIONAL, WORK_LIGHT_ADDITIONAL2, WORK_LIGHT_BACK, WORK_LIGHT_FRONT
```

### `#type`  (15 values)
**Used at 1 location(s):** `vehicle.base.mapHotspot`

```
BOAT, CAR, CUTTER, HARVESTER, HORSE, MOTORBIKE,
OTHER, TOOL, TOOL_TRAILED, TRACTOR, TRAILER, TRAIN,
TRUCK, WHEELLOADER, WOOD_HARVESTER
```

### `#valueType`  (13 values)
**Used at 1 location(s):** `vehicle.drivable.dashboards.dashboard`

```
ac_decelerationAxis, accelerationAxis, combinedPedalLeft, combinedPedalRight, cruiseControl, cruiseControlActive,
cruiseControlReverse, decelerationAxis, directionBackward, directionForward, movingDirection, odometerMilage,
steeringAngle
```

### `#displayType`  (9 values)
**Used at 23 location(s):** `vehicle.ai.automaticSteering.dashboards.dashboard`; `vehicle.attacherJoints.dashboards.dashboard`; `vehicle.baleCounter.dashboards.dashboard`; `vehicle.boat.dashboards.dashboard`; `vehicle.combine.dashboards.dashboard`; `vehicle.conditionalVehicleAnimations.dashboards.dashboard` …

```
ANIMATION, EMITTER, MULTI_STATE, NUMBER, ROT, SLIDER,
TEXT, TRANS, VISIBILITY
```

### `#type`  (8 values)
**Used at 2 location(s):** `vehicle.connectedAttributes.attribute.source`; `vehicle.connectedAttributes.attribute.target`

```
ANIMATION_TIME, JOINT_LIMIT_ROT, JOINT_LIMIT_TRANS, LOCAL_OFFSET, ROTATION, SHADER_PARAMETER,
SHADER_PARAMETER_PREV, TRANSLATION
```

### `#valueType`  (7 values)
**Used at 1 location(s):** `vehicle.lights.dashboards.dashboard`

```
beaconLight, lightState, turnLight, turnLightAny, turnLightHazard, turnLightLeft,
turnLightRight
```

### `#priority`  (5 values)
**Default:** `MEDIUM`  
**Used at 14 location(s):** `(root)`; `attachSound`; `detachSound`; `vehicle.animations.animation.sound`; `vehicle.animations.animationConfigurations.animationConfiguration.animation.sound`; `vehicle.connectionHoses.sounds.connect` …

```
HIGH, LOW, MEDIUM, VERY_HIGH, VERY_LOW
```

### `#valueType`  (5 values)
**Used at 1 location(s):** `vehicle.enterable.dashboards.dashboard`

```
operatingTime, outsideTemperature, time, timeHours, timeMinutes
```

### `(element text)`  (5 values)
**Used at 1 location(s):** `vehicle.storeData.species`

```
ANIMAL, HANDTOOL, OBJECT, PLACEABLE, VEHICLE
```

### `#speedScaleType`  (4 values)
**Used at 3 location(s):** `vehicle.conditionalAnimation.item.clips`; `vehicle.pushHandTool.playerConditionalAnimation.item.clips`; `vehicle.riderConditionalAnimation.item.clips`

```
angular, distance, fixed, none
```

### `#lightType`  (4 values)
**Used at 2 location(s):** `vehicle.lights.sharedLight.function`; `vehicle.lights.staticLightCompounds.staticLightCompound.function`

```
BLINKING, MULTI_BLINK, SLIDE, STATIC
```

### `#valueType`  (4 values)
**Used at 1 location(s):** `vehicle.ai.automaticSteering.dashboards.dashboard`

```
heading, headingLetter, steeringEngaged, steeringState
```

### `#valueType`  (4 values)
**Used at 1 location(s):** `vehicle.standaloneMotor.dashboards.dashboard`

```
ignitionState, motorTemperature, motorTemperatureWarning, operatingTime
```

### `#valueType`  (3 values)
**Used at 1 location(s):** `vehicle.attacherJoints.dashboards.dashboard`

```
bottomArmPosition, bottomArmPositionMax, bottomArmPositionMin
```

### `#valueType`  (3 values)
**Used at 1 location(s):** `vehicle.boat.dashboards.dashboard`

```
acceleration, heading, steeringAngle
```

### `#valueType`  (3 values)
**Used at 1 location(s):** `vehicle.fillUnit.fillUnitConfigurations.fillUnitConfiguration.fillUnits.fillUnit.dashboard`

```
fillLevel, fillLevelPct, fillLevelWarning
```

### `#valueType`  (3 values)
**Used at 1 location(s):** `vehicle.woodHarvester.dashboards.dashboard`

```
curCutLength, cutLength, diameter
```

### `#blendingParameterType`  (2 values)
**Used at 3 location(s):** `vehicle.conditionalAnimation.item.clips`; `vehicle.pushHandTool.playerConditionalAnimation.item.clips`; `vehicle.riderConditionalAnimation.item.clips`

```
angular, scalar
```

### `#shopDisplayUnit`  (2 values)
**Default:** `LITER`  
**Used at 2 location(s):** `vehicle.fillUnit.fillUnitConfigurations.fillUnitConfiguration.fillUnits.fillUnit`; `vehicle.storeData.specs.capacity`

```
CUBICMETER, LITER
```

### `#valueType`  (2 values)
**Used at 1 location(s):** `vehicle.baleCounter.dashboards.dashboard`

```
lifetimeCounter, sessionCounter
```

### `#valueType`  (2 values)
**Used at 1 location(s):** `vehicle.combine.dashboards.dashboard`

```
workedHectars, workedHectarsSession
```

### `#valueType`  (2 values)
**Used at 1 location(s):** `vehicle.conditionalVehicleAnimations.dashboards.dashboard`

```
conditionStateInput, conditionalAnimationState
```

### `#valueType`  (2 values)
**Used at 1 location(s):** `vehicle.dischargeable.dashboards.dashboard`

```
activeDischargeNode, dischargeState
```

### `#preset`  (2 values)
**Default:** `SOWINGMACHINE`  
**Used at 1 location(s):** `vehicle.randomlyMovingParts.randomlyMovingPart`

```
CULTIVATOR, SOWINGMACHINE
```

### `#valueType`  (2 values)
**Used at 1 location(s):** `vehicle.turnOnVehicle.dashboards.dashboard`

```
rpm, turnedOn
```

### `#valueType`  (2 values)
**Used at 1 location(s):** `vehicle.wheels.dashboards.dashboard`

```
brake, steeringAngle
```

### `#valueType`  (1 values)
**Used at 4 location(s):** `vehicle.crabSteering.dashboards.dashboard`; `vehicle.powerTakeOffs.output.dashboard`; `vehicle.powerTakeOffs.powerTakeOffConfigurations.powerTakeOffConfiguration.output.dashboard`; `vehicle.wipers.dashboards.dashboard`

```
state
```

### `#valueType`  (1 values)
**Used at 2 location(s):** `vehicle.cylindered.cylinderedConfigurations.cylinderedConfiguration.dashboards.dashboard`; `vehicle.cylindered.dashboards.dashboard`

```
movingTool
```

---

## Part 2 — Registry-backed string values (the `jointType` gap)

These attributes are typed `String` in the docs but only accept registered values. Source file and base/DLC origin noted per registry.

### `jointType` — attacher joint type
**Vehicle-XML key(s):** `attacherJoint#jointType`, `inputAttacherJoint#jointType` (and combine/cutter joints)  
**Source:** `dataS/scripts/vehicles/specializations/AttacherJoints.lua (AttacherJoints.registerJointType)`  
**Count:** 22 (base game)

The int value of each = registration order (implement=1 … train=22). Default when omitted: `implement`. Mods can register more via `AttacherJoints.registerJointType`.

```
implement, trailer, trailerLow, trailerSaddled, trailerCar, telehandler,
frontloader, loaderFork, semitrailer, semitrailerHook, semitrailerCar, attachableFrontloader,
wheelLoader, manureBarrel, cutter, cutterHarvester, cutterTrailer, skidSteer,
conveyor, hookLift, bigBag, train
```

### `fillType` / `fillTypes` — fill type names
**Vehicle-XML key(s):** `#fillType`, `<fillTypes>` lists, fillUnit/discharge/sprayer fill refs (≈43 spots)  
**Source:** `data/maps/maps_fillTypes.xml`  
**Count:** 176 (base game) + DLC additions below

Case-sensitive UPPERCASE names. Maps and mods add their own fill types; these are the base-game set. Names are also what `densityMapHeightType`, `fillTypeCategory` membership, and most fill-unit refs use.

```
WHEAT, BARLEY, OAT, CANOLA, SORGHUM, SUNFLOWER,
SOYBEAN, MAIZE, POTATO, SUGARBEET, BEETROOT, CARROT,
PARSNIP, COTTON, RICELONGGRAIN, RICE, GREENBEAN, PEA,
SPINACH, SUGARCANE, WOOD, WOODCHIPS, SUGARBEET_CUT, SILAGE,
GRASS, MEADOW, GRASS_WINDROW, DRYGRASS, DRYGRASS_WINDROW, STRAW,
WHEAT_CUT, BARLEY_CUT, OAT_CUT, CANOLA_CUT, SOYBEAN_CUT, GRAPE,
OLIVE, MILK, GOATMILK, BUFFALOMILK, WOOL, EGG,
LIQUIDSEEDTREATMENT, HONEY, LETTUCE, TOMATO, STRAWBERRY, SPRING_ONION,
NAPACABBAGE, CHILLI, GARLIC, ENOKI, OYSTER, BOARDS,
PLANKS, WOODBEAM, PREFABWALL, FLOUR, RICEFLOUR, BREAD,
CAKE, MILK_BOTTLED, GOATMILK_BOTTLED, BUFFALOMILK_BOTTLED, BUTTER, CHEESE,
BUFFALOMOZZARELLA, GOATCHEESE, CHOCOLATE, POTATOCHIPS, RICEROLLS, FERMENTEDNAPACABBAGE,
PRESERVEDCARROTS, PRESERVEDPARSNIP, PRESERVEDBEETROOT, NOODLESOUP, SOUPCANSMIXED, SOUPCANSCARROTS,
SOUPCANSPARSNIP, SOUPCANSBEETROOT, SOUPCANSPOTATO, FABRIC, CLOTHES, SUGAR,
CEREAL, FURNITURE, CARTONROLL, PAPERROLL, PIANO, WAGON,
TOYTRACTOR, SUNFLOWER_OIL, CANOLA_OIL, OLIVE_OIL, RICE_OIL, RAISINS,
GRAPEJUICE, CEMENT, BARREL, BATHTUB, BUCKET, ROOFPLATES,
ROPE, CANNED_PEAS, CEMENTBRICKS, SPINACH_BAGS, JARRED_GREENBEAN, RICE_BAGS,
RICE_BOXES, SEEDS, STONE, MANURE, LIQUIDMANURE, DIGESTATE,
FORAGE, FORAGE_MIXING, WATER, CHAFF, TREESAPLINGS, TREE,
OILSEEDRADISH, POPLAR, DIESEL, DEF, AIR, ELECTRICCHARGE,
METHANE, SNOW, ROADSALT, ROUNDBALE, ROUNDBALE_GRASS, ROUNDBALE_DRYGRASS,
ROUNDBALE_COTTON, ROUNDBALE_WOOD, SQUAREBALE, SQUAREBALE_GRASS, SQUAREBALE_DRYGRASS, SQUAREBALE_COTTON,
SQUAREBALE_WOOD, BALE_WRAP, BALE_NET, BALE_TWINE, RICESAPLINGS, FERTILIZER,
LIQUIDFERTILIZER, PIGFOOD, TARP, LIME, HERBICIDE, SILAGE_ADDITIVE,
MINERAL_FEED, WEED, HORSE_PALOMINO, HORSE_BLACK, HORSE_BAY, HORSE_PINTO,
HORSE_SEAL_BROWN, HORSE_GRAY, HORSE_DUN, HORSE_CHESTNUT, COW_SWISS_BROWN, COW_HOLSTEIN,
COW_LIMOUSIN, COW_ANGUS, COW_WATERBUFFALO, COW_HIGHLAND_CATTLE, SHEEP_LANDRACE, SHEEP_SWISS_MOUNTAIN,
SHEEP_STEINSCHAF, SHEEP_BLACK_WELSH, PIG_LANDRACE, PIG_BLACK_PIED, PIG_BERKSHIRE, CHICKEN,
CHICKEN_ROOSTER, GOAT
```

**+ `highlandsFishingPack` DLC adds 13:**
```
COAL, STONEBIG, CASTLEROCK, SHINGLEROOF, FISHFOOD, SALMONYOUNG,
SALMON, TROUTYOUNG, TROUT, FRIEDONION, ONIONBAG, ONIONSALT,
ONIONSOUP
```

### `fillTypeCategories` — fill type category names
**Vehicle-XML key(s):** `#fillTypeCategories` (space-separated list; expands to member fill types)  
**Source:** `data/maps/maps_fillTypes.xml → <fillTypeCategories>`  
**Count:** 35 (base game)

Use these as shorthand for a group of fill types (e.g. `BULK`, `LIQUID`). They expand to their member `fillType`s.

```
BULK, LIQUID, PIECE, WINDROW, COMBINE, SPRAYER,
SPREADER, MIXERWAGON, AUGERWAGON, FORAGEWAGON, SILAGETRAILER, TRAINWAGON,
FORAGEHARVESTER, SLURRYTANK, MANURESPREADER, MANURESPREADER_ORCHARDS, FORK, SHOVEL,
ANIMAL, HORSE, FARMSILO, HAYLOFT, LOADINGVEHICLE, PRODUCT,
PRODUCT_BGA, VEGETABLES, ROOT_CROPS, TOPLIFTINGHARVESTER, PLANTER_SMALL, ROOTCROP_BELT,
SELLINGSTATION_FIELDFRUITS, SELLINGSTATION_PRODUCTS, SELLINGSTATION_PRODUCTSFOOD, SELLINGSTATION_BALES, SELLINGSTATION_WOOD
```

### `fruitType` — fruit (crop) type names
**Vehicle-XML key(s):** `#fruitType`, cutter/header `<fruitTypes>`, fruitPreparer, planter refs  
**Source:** `data/maps/maps_fruitTypes.xml → data/foliage/<crop>/<crop>.xml`  
**Count:** 25 (base game)
**Case-insensitive** — the game upper/normalizes the XML string before lookup.  

Registered names are camelCase (`sugarBeet`, `riceLongGrain`), **but lookups are case-insensitive** — base vehicle XML uses both `GRAPE` and `canola`. 25 base crops.

```
wheat, barley, canola, oat, maize, sunflower,
soybean, potato, rice, riceLongGrain, sugarBeet, sugarCane,
cotton, sorghum, grape, olive, poplar, beetRoot,
carrot, parsnip, greenBean, pea, spinach, grass,
oilseedRadish
```

### `sprayType` — sprayer/spreader spray types
**Vehicle-XML key(s):** `sprayer#sprayType`, spray fill conversions  
**Source:** `data/maps/maps_sprayTypes.xml`  
**Count:** 7 (base game)

```
FERTILIZER, LIQUIDFERTILIZER, MANURE, LIQUIDMANURE, DIGESTATE, LIME,
HERBICIDE
```

### `densityMapHeightType` (by `fillTypeName`) — heap/tip height types
**Vehicle-XML key(s):** tip/heap height refs keyed by fill type name  
**Source:** `data/maps/maps_densityMapHeightTypes.xml`  
**Count:** 48 (base game)

These are the fill types that have a defined physical heap/height profile (what can be tipped into a heap). Keyed by `fillTypeName`.

```
WHEAT, BARLEY, OAT, CANOLA, SORGHUM, GRAPE,
MAIZE, POTATO, SUGARBEET, SUGARBEET_CUT, BEETROOT, CARROT,
PARSNIP, COTTON, RICELONGGRAIN, RICE, GREENBEAN, PEA,
SPINACH, SOYBEAN, SUNFLOWER, CHAFF, POPLAR, SEEDS,
LIME, MINERAL_FEED, FERTILIZER, SUGARCANE, STRAW, WHEAT_CUT,
BARLEY_CUT, OAT_CUT, CANOLA_CUT, SOYBEAN_CUT, GRASS_WINDROW, DRYGRASS_WINDROW,
SILAGE, FORAGE, PIGFOOD, MANURE, LIQUIDMANURE, WOODCHIPS,
TARP, SNOW, ROADSALT, STONE, OLIVE, DIGESTATE,
```

### `workArea#type` — work area types
**Vehicle-XML key(s):** `workAreas.workArea#type`  
**Source:** `dataS/scripts/vehicles/**/*.lua (g_workAreaTypeManager:addWorkAreaType)`  
**Count:** 25 (base game)

Default when omitted: `default`.

```
auxiliary, baler, combineChopper, combineSwath, cultivator, cutter,
default, forageWagon, fruitPreparer, haulmDrop, mower, mulcher,
plow, plowShare, ridgeFormer, ridgemarker, roller, saltSpreader,
sowingMachine, sprayer, stonePicker, stumpCutter, tedder, weeder,
windrower
```

### `rigidBodyTypeActive` / `rigidBodyTypeInactive` — physics body type
**Vehicle-XML key(s):** objectChange `#rigidBodyTypeActive`, `#rigidBodyTypeInactive`  
**Source:** `engine enum RigidBodyType (parsed via RigidBodyType[string.upper(str)] in ObjectChangeUtil.lua)`  
**Count:** 4 (base game)
**Case-insensitive** — the game upper/normalizes the XML string before lookup.  

```
NONE, STATIC, DYNAMIC, KINEMATIC
```

### `particleType` — particle system type
**Vehicle-XML key(s):** particle/effect `#particleType`  
**Source:** `dataS/scripts/materials/ParticleSystemManager.lua (addParticleType)`  
**Count:** 42 (base game)

```
unloading, smoke, smoke_damping, smoke_chimney, smoke_train_main, smoke_train_side,
chopper, straw, cutter_chopper, soil, soil_smoke, soil_chunks,
soil_big_chunks, soil_harvesting, spreader, spreader_smoke, windrower, tedder,
weeder, crusher_wood, crusher_dust, prepare_fruit, cleaning_soil, cleaning_dust,
washer_water, chainsaw_wood, chainsaw_dust, pickup, pickup_falling, sowing,
loading, wheel_dust, wheel_dry, wheel_wet, wheel_snow, bees,
horse_step_slow, horse_step_fast, spraycan_paint, HYDRAULIC_HAMMER, HYDRAULIC_HAMMER_DEBRIS, STONE,
```

### `effectClass` — effect implementation class
**Vehicle-XML key(s):** `effectNode#effectClass`, `<effects>` entries  
**Source:** `dataS/scripts/effects/*.lua (resolved via ClassUtil.getClassObject — any loaded Effect subclass)`  
**Count:** 20 (base game)

**Open set.** Unlike the others, `effectClass` accepts ANY globally-registered class derived from `Effect`. Below are the base-game Effect subclasses; mods can add more (referenced as `ModName.MyEffect`). Default: `ShaderPlaneEffect`.

```
ConveyorBeltEffect, CultivatorMotionPathEffect, CutterMotionPathEffect, ExhaustEffect, FertilizerMotionPathEffect, GrainTankEffect,
LevelerEffect, MorphPositionEffect, MotionPathEffect, ParticleEffect, PipeEffect, PlowMotionPathEffect,
ShaderPlaneEffect, SlurrySideToSideEffect, SnowPlowMotionPathEffect, TipEffect, TypedMotionPathEffect, VariableMotionPathEffect,
WindrowerEffect, WindrowerMotionPathEffect
```

### Connection hoses — `connectionHoses` registry
**Source:** `data/shared/connectionHoses/connectionHoses.xml` (g_connectionHoseManager)  

**`connectionHoseType` / hose `#type` (18):**
```
airDoubleRed, airDoubleYellow, hydraulicIn, hydraulicOut,
electric, electricType2, isobus, TOOL_CONNECTOR_TOP_RIGHT,
TOOL_CONNECTOR_TOP_RIGHT_02, TOOL_CONNECTOR_BOTTOM_01, TOOL_CONNECTOR_BOTTOM_02, TOOL_CONNECTOR_BOTTOM_03,
TOOL_CONNECTOR_BOTTOM_04, TOOL_CONNECTOR_VADERSTAD_PROCEEDV_01, TOOL_CONNECTOR_VADERSTAD_PROCEEDV_02, TOOL_CONNECTOR_VADERSTAD_PROCEEDV_03,
TOOL_CONNECTOR_VADERSTAD_PROCEEDV_04, CABLE_BUNDLE
```

**`adapter#name` / adapterType (2):** `DEFAULT`, `METAL`

**`socket#name` (10):**
```
electric, electric_metal, hydraulic01, hydraulic02,
air_yellow, air_red, hydraulic03, hydraulic04,
isobus, electricType2
```

**`material#name` (5):** `CLOTH`, `DEFAULT`, `JOHNDEERE`, `LABELLED`, `RUBBER`

### `inputAction` / input binding names
**Vehicle-XML key(s):** `#inputAction`, `actionBinding`, `<inputAttacherJoint>` action refs  
**Source:** `dataS/inputActions.xml`  
**Count:** 254 (base game)

Base-game input action names. Mods register their own via modDesc `<inputBinding>`.

```
AXIS_MOVE_FORWARD_PLAYER, AXIS_MOVE_SIDE_PLAYER, AXIS_LOOK_UPDOWN_PLAYER, AXIS_LOOK_LEFTRIGHT_PLAYER, AXIS_RUN,
TOGGLE_CONSTRUCTION, AXIS_ACCELERATE_VEHICLE, AXIS_BRAKE_VEHICLE, AXIS_MOVE_SIDE_VEHICLE, AXIS_LOOK_UPDOWN_VEHICLE,
AXIS_LOOK_LEFTRIGHT_VEHICLE, AXIS_WHEEL_BASE, AXIS_CRUISE_CONTROL, AXIS_ROTATE_HANDTOOL, AXIS_PITCH_HANDTOOL,
MENU_AXIS_UP_DOWN, MENU_AXIS_UP_DOWN_SECONDARY, MENU_AXIS_LEFT_RIGHT, AXIS_HYDRAULICATTACHER1, AXIS_HYDRAULICATTACHER2,
AXIS_CUTTER_REEL, AXIS_CUTTER_REEL2, AXIS_SPRAYER_ARM, AXIS_FRONTLOADER_ARM, AXIS_FRONTLOADER_ARM2,
AXIS_FRONTLOADER_TOOL, AXIS_FRONTLOADER_TOOL2, AXIS_FRONTLOADER_TOOL3, AXIS_FRONTLOADER_TOOL4, AXIS_FRONTLOADER_TOOL5,
AXIS_CRANE_ARM, AXIS_CRANE_ARM2, AXIS_CRANE_ARM3, AXIS_CRANE_ARM4, AXIS_CRANE_TOOL,
AXIS_CRANE_TOOL2, AXIS_CRANE_TOOL3, AXIS_CRANE_SUPPORT, AXIS_DOOR, AXIS_DOOR_2,
AXIS_DOOR_3, AXIS_PIPE, AXIS_PIPE2, AXIS_DRAWBAR, AXIS_DRAWBAR2,
AXIS_MAP_ZOOM_IN, AXIS_MAP_ZOOM_OUT, AXIS_MAP_SCROLL_LEFT_RIGHT, AXIS_MAP_SCROLL_UP_DOWN, AXIS_PICK_COLOR_UPDOWN,
AXIS_PICK_COLOR_LEFTRIGHT, JUMP, INTERACT, ENTER, SWITCH_SEAT,
CROUCH, CAMERA_SWITCH, ACTIVATE_OBJECT, ANIMAL_PET, CYCLE_HANDTOOL,
TOGGLE_HANDTOOL, ACTIVATE_HANDTOOL, ACTIVATE_HANDTOOL_SECONDARY, HANDS_LEVEL, ROTATE_OBJECT_LEFT_RIGHT,
ROTATE_OBJECT_UP_DOWN, SPRAYCAN_CHANGE_MARKER, TOGGLE_LIGHTS_FPS, THROW_OBJECT, PAUSE,
SKIP_MESSAGE_BOX, CAMERA_ZOOM_IN_OUT, SWITCH_VEHICLE, SWITCH_VEHICLE_BACK, MENU,
TOGGLE_STORE, TOGGLE_MAP, TOGGLE_CHARACTER_CREATION, TOGGLE_HELP, PUSH_TO_TALK,
ATTACH, DETACH, SWITCH_IMPLEMENT, SWITCH_IMPLEMENT_BACK, TOGGLE_AI,
TOGGLE_AI_STEERING, TOGGLE_AI_STEERING_LINES, AXIS_CONSTRUCTION_CAMERA_ZOOM, AXIS_CONSTRUCTION_CAMERA_ROTATE, AXIS_CONSTRUCTION_CAMERA_TILT,
AXIS_CONSTRUCTION_CURSOR_ROTATE, CONSTRUCTION_ACTION_PRIMARY, CONSTRUCTION_ACTION_SECONDARY, CONSTRUCTION_ACTION_TERTIARY, CONSTRUCTION_ACTION_FOURTH,
CONSTRUCTION_ACTION_SNAPPING, AXIS_CONSTRUCTION_ACTION_PRIMARY, AXIS_CONSTRUCTION_ACTION_SECONDARY, AXIS_CONSTRUCTION_MENU_UP_DOWN, AXIS_CONSTRUCTION_MENU_LEFT_RIGHT,
CONSTRUCTION_DESTRUCT_TOGGLE, CONSTRUCTION_SHOW_CONFIGS, AXIS_MTO_SCROLL, HONK, MOTOR_STATE_ON,
MOTOR_STATE_OFF, MOTOR_STATE_IGNITION, TOGGLE_MOTOR_STATE, AXIS_CLUTCH_VEHICLE, SHIFT_GEAR_UP,
SHIFT_GEAR_DOWN, SHIFT_GEAR_SELECT_1, SHIFT_GEAR_SELECT_2, SHIFT_GEAR_SELECT_3, SHIFT_GEAR_SELECT_4,
SHIFT_GEAR_SELECT_5, SHIFT_GEAR_SELECT_6, SHIFT_GEAR_SELECT_7, SHIFT_GEAR_SELECT_8, SHIFT_GROUP_UP,
SHIFT_GROUP_DOWN, SHIFT_GROUP_SELECT_1, SHIFT_GROUP_SELECT_2, SHIFT_GROUP_SELECT_3, SHIFT_GROUP_SELECT_4,
DIRECTION_CHANGE, DIRECTION_CHANGE_POS, DIRECTION_CHANGE_NEG, TOGGLE_TIPSTATE, TOGGLE_LIGHTS,
TOGGLE_LIGHTS_BACK, TOGGLE_LIGHTS_EXTERNAL, TOGGLE_BEACON_LIGHTS, TOGGLE_TIPSIDE, TOGGLE_TURNLIGHT_LEFT,
TOGGLE_TURNLIGHT_RIGHT, TOGGLE_CRABSTEERING, TOGGLE_CRABSTEERING_BACK, TOGGLE_WORKMODE, TOGGLE_TENSION_BELTS,
TOGGLE_BALE_TYPES, BALE_COUNTER_RESET, BALE_WRAPPER_DROP_CUSTOM, VEHICLE_ACTION_CONTROL, LOWER_IMPLEMENT,
IMPLEMENT_EXTRA, IMPLEMENT_EXTRA2, IMPLEMENT_EXTRA3, IMPLEMENT_EXTRA4, FOLDABLESTEPS_NEXT_POS,
FOLDABLESTEPS_NEXT_NEG, DOUBLED_SPRAY_AMOUNT, TOGGLE_SEEDS, TOGGLE_SEEDS_BACK, TOGGLE_PIPE,
TOGGLE_COVER, TOGGLE_CHOPPER, TOGGLE_MAP_SIZE, VARIABLE_WORK_WIDTH_LEFT, VARIABLE_WORK_WIDTH_RIGHT,
VARIABLE_WORK_WIDTH_TOGGLE, TOGGLE_CUT_LENGTH_BACK, WOOD_HARVESTER_DROP, TREE_AUTOMATIC_ALIGN, TOGGLE_WOOD_HARVESTER_TILT,
YARDER_CONTROL_LEFTRIGHT, YARDER_CONTROL_UPDOWN, YARDER_FOLLOW_ME, YARDER_FOLLOW_HOME, YARDER_FOLLOW_PICKUP,
YARDER_ATTACH, YARDER_DETACH, YARDER_SETUP_ROPE, WINCH_CONTROL, WINCH_CONTROL_VEHICLE,
WINCH_ATTACH_MODE, WINCH_ATTACH, WINCH_DETACH, PALLET_FILLER_BUY_PALLETS, CHANGE_DRIVING_DIRECTION,
TOGGLE_TIPSTATE_GROUND, TOGGLE_CRUISE_CONTROL, RADIO_TOGGLE, RADIO_NEXT_CHANNEL, RADIO_PREVIOUS_CHANNEL,
RADIO_NEXT_ITEM, RADIO_PREVIOUS_ITEM, CONVERSATION_SKIP, INTRODUCTION_HELP_SKIP, INGAMEMAP_ACCEPT,
MENU_ACTIVATE, MENU_ACCEPT, MENU_CANCEL, MENU_BACK, MENU_EXTRA_1,
MENU_EXTRA_2, MENU_PAGE_PREV, MENU_PAGE_NEXT, MENU_LIST_PAGE_START, MENU_LIST_PAGE_END,
MENU_LIST_PAGE_PREV, MENU_LIST_PAGE_NEXT, MENU_LIST_PAGE_START_GAMEPAD, MENU_LIST_PAGE_END_GAMEPAD, MENU_MAP_ACTION_1,
TAKE_SCREENSHOT, CHAT, TOGGLE_TURNLIGHT_HAZARD, TOGGLE_WORK_LIGHT_BACK, TOGGLE_WORK_LIGHT_FRONT,
TOGGLE_HIGH_BEAM_LIGHT, TOGGLE_LIGHT_FRONT, LOWER_ALL_IMPLEMENTS, TURN_ON_ALL_IMPLEMENTS, FOLD_ALL_IMPLEMENTS,
TOGGLE_HELP_TEXT, INCREASE_TIMESCALE, DECREASE_TIMESCALE, CRABSTEERING_ALLWHEEL, CRABSTEERING_CRABLEFT,
CRABSTEERING_CRABRIGHT, WORKMODE_MIDDLE, WORKMODE_LEFT, WORKMODE_RIGHT, RESET_HEAD_TRACKING,
UNLOAD, DEBUG_PLAYER_UP_DOWN, DEBUG_PLAYER_ENABLE, DEBUG_VEHICLE_1, DEBUG_VEHICLE_2,
DEBUG_VEHICLE_3, DEBUG_VEHICLE_4, DEBUG_VEHICLE_5, DEBUG_VEHICLE_6, DEBUG_VEHICLE_7,
DEBUG_VEHICLE_8, DEBUG_VEHICLE_9, CONSOLE_ALT_COMMAND_BUTTON, CONSOLE_ALT_COMMAND2_BUTTON, CONSOLE_ALT_COMMAND3_BUTTON,
CONSOLE_DEBUG_TOGGLE_FPS, CONSOLE_DEBUG_TOGGLE_STATS, CONSOLE_DEBUG_FILLUNIT_NEXT, CONSOLE_DEBUG_FILLUNIT_INC, CONSOLE_DEBUG_FILLUNIT_DEC,
ADD_NOTE, MOUSE_ALT_COMMAND_BUTTON, MOUSE_ALT_COMMAND2_BUTTON, MOUSE_ALT_COMMAND3_BUTTON, MOUSE_ALT_COMMAND4_BUTTON,
AXIS_LOOK_LEFTRIGHT_DRAG, AXIS_LOOK_UPDOWN_DRAG, RELOAD_GAME, GAMING_STATION_TOGGLE_LANGUAGE
```

### `vehicleBrand` / `brand` — brand id
**Vehicle-XML key(s):** `storeData.brand`, brand-keyed material templates  
**Source:** `dataS/brands.xml`  
**Count:** 260 (base game)

No DLC-exclusive brands were found in the unpacked packs — DLC vehicles reuse these base ids. `NONE` is the unbranded sentinel.

```
ABI, AEBI, AGI, AGIWESTFIELD, AGIBATCO, AGINECO,
AGIWESTEEL, AGISTORM, AGISENTINEL, AGCO, AGRIFAC, AGRIO,
AGRISEM, AGRISPREAD, AGROMASZ, ALBUTT, ALDI, ALLIANCE,
ALPEGO, AMAZONE, AMITYTECH, ANDERSONGROUP, ANNABURGER, APV,
ANTONIOCARRARO, APE, APRILIA, ARCUSIN, ARMATRAC, BEDNAR,
BERGMANN, BERTHOUD, BKT, BOECKMANN, BOMECH, BOURGAULT,
BRANDT, BRANTNER, BREDAL, BREMER, BRIELMAIER, BRIRI,
BUEHRER, BUNNING, CANAM, CAPELLO, CASEIH, CHALLENGER,
CLAAS, CONTINENTAL, CONVEYALL, CORTEVA, DALBO, DAMCON,
DAMMANN, DEGELMAN, DEMCO, DEUTZFAHR, DEWULF, DFM,
DUEVELSDORF, EASYSHEDS, EINBOECK, ELHO, ELMERSMFG, EVERSAGRO,
SKODA, STRAUSS, ELTEN, ERO, FARESIN, FARMAX,
FARMET, FARMTECH, FENDT, FIAT, FLEXICOIL, FLIEGL,
FMZ, FORD, FORTSCHRITT, FORTUNA, FSI, FUHRMANN,
GALAXY, GEA, GERINGHOFF, GESSNER, GIANTS, GOEWEIL,
GOLDHOFER, GORENC, GREATPLAINS, GREGOIRE, GREGOIREBESSON, GRIMME,
GROHA, HARDI, HATZENBICHLER, HAUER, HAWE, HEIZOMAT,
HELM, HOLARAS, HOLMER, HORSCH, HUSQVARNA, IMPEX,
INTERNATIONAL, ISEKI, JCB, JENZ, JMMANUFACTURING, JOHNDEERE,
JONSERED, JOSKIN, JUNGHEINRICH, KAERCHER, KAWECO, KESLA,
KEMPER, KINGSTON, KINZE, KLINE, KNOCHE, KOCKERLING,
KOLLER, KOMATSU, KONGSKILDE, KOTSCHENREUTHER, KOTTE, KRAMER,
KRAMPE, KROEGER, KRONE, KRONETRAILER, KUBOTA, KUHN,
KVERNELAND, LACOTEC, LANDINI, LELY, LEMKEN, LINDNER,
LIZARD, NONE, LODEKING, MACDON, MACK, MAGSI,
MAHINDRA, MAN, MANITOU, MASSEYFERGUSON, MCCORMACK, MCCORMICK,
MCCULLOCH, MERCEDESBENZTRUCKS, MERIDIAN, MERLO, MICHELIN, MICHIELETTO,
MITAS, MONOSEM, MZURI, NARDI, NEUERO, NEWHOLLAND,
NEXAT, NOKIAN, NORDSTEN, NOVAG, OLOFSFORS, OXBO,
PALADIN, PESSLINSTRUMENTS, PFANZELT, PIONEER, PLANET, PLOEGER,
POETTINGER, PONSSE, PORSCHEDIESEL, PRINOTH, PROVITIS, QUICKE,
RABE, RANDON, RANIPLAST, RAU, REITER, RIEDLER,
RIGITRAC, RISUTEC, ROPA, ROSTSELMASH, ROTTNE, RUDOLFHOERMANN,
RUDOLPH, SALEK, SALFORD, SAMASZ, SAME, SAMPOROSENLEW,
SAMSONAGRO, SCHAEFFER, SCHOUTEN, SCHUITEMAKER, SCHWARZMUELLER, SENNEBOGEN,
SEPPKNUSEL, SILOKING, SIP, SIRCH, STADIA, STARA,
STARKINDUSTRIES, STEMA, STEPA, STEYR, STIHL, STOLL,
STRAUTMANN, STREUMASTER, SUER, SUMMERSMFG, TAJFUN, TATRA,
TENWINKEL, THUERINGERAGRAR, THUNDERCREEK, TMCCANCELA, TREFFLER, TRELLEBORG,
TROUTRIVER, TT, UNIA, UNVERFERTH, VAEDERSTAD, VALTRA,
VEENHUIS, VERMEER, VERSATILE, VERVAET, VICON, VOLVO,
VREDESTEIN, VREDO, PITTSTRAILERS, WALKABOUT, WARZEE, WEBERMT,
WELGER, WESTTECH, WIFO, WILSON, WIENHOFF, ZETOR,
ZIEGLER, ZUNHAMMER
```

### `storeData.category` — shop categories
**Source:** `dataS/storeCategories.xml`  

**Category *types* (top-level grouping, 20):**
```
DRIVABLES, LOADERS, TRAILERS, SOIL_PREPARATION, SEEDING,
YIELD, COMBINE, FORAGE, GRASSLAND, BALING,
ROOTCROPS, VEGETABLES, SPECIALCROPS, GRAPES_OLIVES, ANIMALS,
FORESTRY, MISC, OBJECTS, HANDTOOLS, PLACEABLE,
```

**Category names (what a vehicle's `<category>` uses, 147):**
```
tractorsS, tractorsM, tractorsL, trucks, cars,
miscDrivables, frontLoaderVehicles, frontLoaders, frontLoaderTools, teleLoaderVehicles,
teleLoaderTools, wheelLoaderVehicles, wheelLoaderTools, skidSteerVehicles, skidSteerTools,
forklifts, trailers, augerWagons, trailersChangingSystem, trailersFlatbed,
lowloaders, trailersSemi, plows, cultivators, discHarrows,
powerHarrows, subsoilers, mulchers, spaders, stonePickers,
seeders, planters, seedTanks, palletSeeds, sprayers,
manureSpreaders, fertilizerSpreaders, slurryTanks, slurryTools, slurryTransport,
weeders, rollers, palletFertilizerHerbicide, harvesters, cutters,
cornHeaders, specialHeaders, cutterTrailers, combineWindrower, forageHarvesters,
forageHarvesterCutters, forageHarvesterCutterTrailers, leveler, silocompaction, palletSilage,
mowers, tedders, windrowers, loaderWagons, grasslandCare,
palletGrassland, balersSquare, balersRound, baleLoaders, baleWrappers,
balingMisc, palletBaling, forageMixers, barrels, animalTransport,
strawBlowers, palletAnimals, beetHarvesters, beetHarvesterCutters, beetLoading,
potatoPlanting, potatoHarvesting, palletSeedsRootcrops, vegetablePlanters, vegetableHarvesters,
spinachHarvesters, greenBeanHarvesters, peaHarvesters, palletVegetables, ricePlanters,
riceHarvesters, sugarcanePlanters, sugarcaneHarvesters, sugarcaneTransport, cottonHarvesters,
cottonTransport, specialCropsPallets, oliveHarvesters, grapeHarvesters, grapeTrailers,
grapeTools, forestryHarvesters, forestryForwarders, forestryExcavators, forestryExcavatorTools,
woodTransport, woodChippers, forestryMulchers, forestryWinches, forestryPlanters,
forestryStumpCutters, forestryMisc, palletForestry, weights, belts,
winterEquipment, carTrailers, misc, bigbags, bigbagPallets,
ibc, pallets, bales, shippingContainers, objectAnimal,
objectMisc, chainsaws, shovels, flashlights, markingSpray,
handtoolsAnimals, handtoolsMisc, animalpens, fences, trees,
storages, containers, dieselTanks, waterTanks, fillableTanks,
silos, siloExtensions, sheds, gardenSheds, farmhouses,
beeHives, generators, floodLighting, decoration, productionPoints,
sellingPoints, placeableMisc
```

### `materialTemplateName` / `defaultColorMaterialTemplateName` — material templates
**Source:** `data/shared/detailLibrary/materialTemplates.xml` (generic) + `data/shared/brandMaterialTemplates.xml` (brand colors)  

> Note: `materialSlotName` is **not** an enum — it is an arbitrary per-model material slot name baked into each vehicle's i3d, so there is no global list. `materialTemplateName` IS a closed registry, below.

**Generic material templates (104):**
```
chrome, silverScratched, silverScratchedShiny, brassScratched,
bronzeScratched, copperScratched, goldScratched, palladiumScratched,
silverRough, silverBumpy, metalGalvanized, zincGalvanized,
silverCircularBrushed, steelTreadPlate, metalPainted, metalPaintedBlack,
metalPaintedGray, metalPaintedRough, metalPaintedRoughBlack, metalPaintedRoughGray,
metalPaintedGraphite, metalPaintedGraphiteBlack, metalPaintedOld, metalPaintedOldGray,
plasticPainted, plasticPaintedBlack, plasticPaintedGray, plasticPaintedShinyBlack,
plasticPaintedShinyGray, plasticGearShift, plasticGearShiftGrayDark, plasticLeatherGrainMedium,
plasticLeatherGrainSmall, plasticGraniteGrainSmall, plasticGraniteGrainSmallBlack, rubber,
rubberBlack, rubberBlackHoses, wood1, wood1Cedar,
wood2, wood2Oak, leather1, leather1Brown,
leather2, leather2Brown, leather3, leather3GrayDark,
perforatedSynthetic1, perforatedSynthetic1Black, perforatedSynthetic2, perforatedSynthetic2Black,
fabric1, fabric1Bluish, fabric2, fabric2Gray,
fabric3, fabric3Gray, fabric4, fabric4Beige,
fabric5, fabric5Dark, fabric6, fabric6Bluish,
fell, fellGray, reflectorWhite, reflectorRed,
reflectorOrange, reflectorYellow, reflectorWhiteHexagon, reflectorRedHexagon,
reflectorOrangeHexagon, reflectorYellowHexagon, reflectorWhiteCube, reflectorRedCube,
reflectorOrangeCube, reflectorYellowCube, reflectorWhiteDaylight, reflectorOrangeDaylight,
dirt, snow, decal, glassClear01,
glassClear02, glassClear03, glassWindow, glassHeadlight,
glassLine01, glassSquare01, halfMetalNoise1, halfMetalNoise1Black,
halfMetalNoise2, calibratedPaint, calibratedPaintBumpy, calibratedGlossPaint,
calibratedMetallic, calibratedMetallicPaint, calibratedCastIron, calibratedMatPaint,
carbonPattern01, carbonPattern02, fabricOrnamental1, powderCoatMatte,
```

**Brand color templates (1133)** — naming pattern `BRAND_COLORn`. Grouped by brand prefix:

<details><summary>Expand full brand-color template list (1133)</summary>

**AEBI** (2): `AEBI_RED1`, `AEBI_WHITE1`
**AGCO** (3): `AGCO_GREY1`, `AGCO_GREY2`, `AGCO_GREY3`
**AGI** (4): `AGI_GREEN1`, `AGI_ORANGE1`, `AGI_RED1`, `AGI_YELLOW1`
**AGRIFAC** (1): `AGRIFAC_RED1`
**AGRIO** (3): `AGRIO_BLUE`, `AGRIO_GREY`, `AGRIO_WHITE`
**AGRISEM** (1): `AGRISEM_YELLOW1`
**AGRISPREAD** (3): `AGRISPREAD_GREY`, `AGRISPREAD_RED`, `AGRISPREAD_WHITE`
**AGROMASZ** (3): `AGROMASZ_GREENPAINT`, `AGROMASZ_REDPAINT`, `AGROMASZ_WHITEPAINT`
**ALBUTT** (5): `ALBUTT_BLACK1`, `ALBUTT_BLUE1`, `ALBUTT_GREEN1`, `ALBUTT_GREY1`, `ALBUTT_RED1`
**ALPEGO** (2): `ALPEGO_BLUE`, `ALPEGO_ORANGE1`
**AMAZONE** (12): `AMAZONE_BEIGE1`, `AMAZONE_BLACK`, `AMAZONE_BLUE1`, `AMAZONE_BLUE2`, `AMAZONE_BLUE3`, `AMAZONE_GREEN1`, `AMAZONE_GREY`, `AMAZONE_ORANGE1`, `AMAZONE_RED1`, `AMAZONE_SILVER`, `AMAZONE_YELLOW1`, `AMAZONE_YELLOW2`
**AMITYTECH** (1): `AMITYTECH_RED1`
**ANDERSONGROUP** (3): `ANDERSONGROUP_GREY1`, `ANDERSONGROUP_RED1`, `ANDERSONGROUP_YELLOW1`
**ANNABURGER** (6): `ANNABURGER_BEIGE1`, `ANNABURGER_BLUE1`, `ANNABURGER_GREEN1`, `ANNABURGER_GREY1`, `ANNABURGER_RED1`, `ANNABURGER_WHITE1`
**ANTONIOCARRARO** (12): `ANTONIOCARRARO_BLACK1`, `ANTONIOCARRARO_BLUE1`, `ANTONIOCARRARO_BLUE2`, `ANTONIOCARRARO_GREEN1`, `ANTONIOCARRARO_GREY1`, `ANTONIOCARRARO_GREY2`, `ANTONIOCARRARO_GREY3`, `ANTONIOCARRARO_ORANGE1`, `ANTONIOCARRARO_ORANGE2`, `ANTONIOCARRARO_PURPLE1`, `ANTONIOCARRARO_RED1`, `ANTONIOCARRARO_RED2`
**APE** (7): `APE_BLACK1`, `APE_BLUE1`, `APE_GREEN1`, `APE_GREY1`, `APE_ORANGE1`, `APE_RED1`, `APE_WHITE1`
**APV** (2): `APV_RED1`, `APV_YELLOW1`
**ARCUSIN** (6): `ARCUSIN_GREY1`, `ARCUSIN_GREY2`, `ARCUSIN_ORANGE1`, `ARCUSIN_RED1`, `ARCUSIN_WHITE`, `ARCUSIN_YELLOW1`
**ARMATRAC** (4): `ARMATRAC_GREEN1`, `ARMATRAC_GREY1`, `ARMATRAC_ORANGE1`, `ARMATRAC_RED1`
**BAUER** (3): `BAUER_GREEN1`, `BAUER_PURPLE`, `BAUER_RED`
**BEDNAR** (5): `BEDNAR_BLUE1`, `BEDNAR_GRAY1`, `BEDNAR_GRAY2`, `BEDNAR_RED1`, `BEDNAR_YELLOW1`
**BERGMANN** (6): `BERGMANN_BRONZE1`, `BERGMANN_GREEN1`, `BERGMANN_GREY01`, `BERGMANN_GREY02`, `BERGMANN_RED1`, `BERGMANN_YELLOW1`
**BERTHOUD** (2): `BERTHOUD_BLUE1`, `BERTHOUD_TURQUOISE1`
**BIGBUD** (7): `BIGBUD_BLUE1`, `BIGBUD_BLUE2`, `BIGBUD_GRAY1`, `BIGBUD_GREEN1`, `BIGBUD_ORANGE1`, `BIGBUD_RED1`, `BIGBUD_YELLOW1`
**BIZON** (9): `BIZON_BEIGE1`, `BIZON_BLACK1`, `BIZON_BLACK2`, `BIZON_DARKGRAY1`, `BIZON_GRAY1`, `BIZON_GRAY2`, `BIZON_GRAY3`, `BIZON_GREEN1`, `BIZON_RED1`
**BOECKMANN** (1): `BOECKMANN_BLUE1`
**BOMECH** (3): `BOMECH_BLUE1`, `BOMECH_GREEN1`, `BOMECH_RED1`
**BOURGAULT** (4): `BOURGAULT_RED1`, `BOURGAULT_WHITE1`, `BOURGAULT_WHITE2`, `BOURGAULT_YELLOW1`
**BRANDT** (5): `BRANDT_BLUE1`, `BRANDT_GREY1`, `BRANDT_GREY2`, `BRANDT_GREY3`, `BRANDT_ORANGE1`
**BRANTNER** (5): `BRANTNER_BLACK`, `BRANTNER_GREEN1`, `BRANTNER_GREEN2`, `BRANTNER_ORANGE1`, `BRANTNER_RED1`
**BREDAL** (3): `BREDAL_GREY`, `BREDAL_RED1`, `BREDAL_YELLOW1`
**BREMER** (1): `BREMER_BLUE1`
**BRIELMAIER** (3): `BRIELMAIER_BLUE1`, `BRIELMAIER_GREY1`, `BRIELMAIER_SILVER1`
**BRIRI** (5): `BRIRI_BLACK1`, `BRIRI_GREEN1`, `BRIRI_GREEN2`, `BRIRI_GREY`, `BRIRI_RED`
**BROCHARD** (3): `BROCHARD_BLUE1`, `BROCHARD_RED1`, `BROCHARD_YELLOW1`
**BUEHRER** (13): `BUEHRER_BLACK1`, `BUEHRER_BLACK2`, `BUEHRER_BLUE1`, `BUEHRER_BLUE2`, `BUEHRER_BLUE3`, `BUEHRER_GREEN1`, `BUEHRER_GREEN2`, `BUEHRER_GREEN3`, `BUEHRER_RED1`, `BUEHRER_RED2`, `BUEHRER_RED3`, `BUEHRER_YELLOW1`, `BUEHRER_YELLOW2`
**BUNNING** (3): `BUNNING_BLACK`, `BUNNING_BLUE`, `BUNNING_GREEN`
**CANAM** (2): `CANAM_COMPASS_GREEN`, `CANAM_FIERYRED`
**CAPELLO** (2): `CAPELLO_BLACK1`, `CAPELLO_RED1`
**CARUELLENICOLAS** (8): `CARUELLENICOLAS_BLACK1`, `CARUELLENICOLAS_BLUE1`, `CARUELLENICOLAS_BLUE2`, `CARUELLENICOLAS_GREY1`, `CARUELLENICOLAS_GREY2`, `CARUELLENICOLAS_GREY3`, `CARUELLENICOLAS_RED1`, `CARUELLENICOLAS_YELLOW1`
**CASEIH** (15): `CASEIH_BEIGE1`, `CASEIH_BEIGE2`, `CASEIH_BEIGE3`, `CASEIH_BEIGE4`, `CASEIH_BLACK`, `CASEIH_BLUE1`, `CASEIH_FARMALL_BEIGE`, `CASEIH_FARMALL_GOLD`, `CASEIH_GREEN1`, `CASEIH_GREY`, `CASEIH_ORANGE1`, `CASEIH_RED1`, `CASEIH_RED2`, `CASEIH_RED3`, `CASEIH_SILVER`
**CHALLENGER** (3): `CHALLENGER_ORANGE1`, `CHALLENGER_RED1`, `CHALLENGER_YELLOW1`
**CLAAS** (8): `CLAAS_DARKGREY1`, `CLAAS_DARKGREY2`, `CLAAS_GREEN1`, `CLAAS_GREY1`, `CLAAS_ORANGE1`, `CLAAS_RED1`, `CLAAS_WHITE1`, `CLAAS_WHITE2`
**DALBO** (1): `DALBO_BLUE1`
**DAMCON** (2): `DAMCON_RED1`, `DAMCON_YELLOW1`
**DAMMANN** (4): `DAMMANN_GREEN`, `DAMMANN_GREY1`, `DAMMANN_GREY2`, `DAMMANN_YELLOW`
**DEGELMAN** (2): `DEGELMAN_YELLOW1`, `DEGELMAN_YELLOW2`
**DEMCO** (6): `DEMCO_BLUE1`, `DEMCO_GREEN1`, `DEMCO_GREY1`, `DEMCO_ORANGE1`, `DEMCO_RED1`, `DEMCO_WHITE1`
**DEUTZ** (19): `DEUTZ_BEIGE1`, `DEUTZ_BLACK1`, `DEUTZ_BLACK2`, `DEUTZ_BLUE6`, `DEUTZ_GREEN1`, `DEUTZ_GREEN4`, `DEUTZ_GREEN5`, `DEUTZ_GREEN6`, `DEUTZ_GREY01`, `DEUTZ_GREY02`, `DEUTZ_GREY03`, `DEUTZ_GREY04`, `DEUTZ_JAVAGREEN`, `DEUTZ_MATTGREEN`, `DEUTZ_ORANGE1`, `DEUTZ_RED1`, `DEUTZ_RED2`, `DEUTZ_WHITE`, `DEUTZ_YELLOW1`
**DEWULF** (2): `DEWULF_GREY1`, `DEWULF_RED1`
**DFM** (4): `DFM_DARKBLUE1`, `DFM_GREEN1`, `DFM_GREEN2`, `DFM_YELLOW1`
**DOBLETT** (10): `DOBLETT_BLACK1`, `DOBLETT_BLACK2`, `DOBLETT_BLUE1`, `DOBLETT_DARKGRAY1`, `DOBLETT_GRAY1`, `DOBLETT_GRAY2`, `DOBLETT_GREEN1`, `DOBLETT_ORANGE1`, `DOBLETT_RED1`, `DOBLETT_YELLOW1`
**DUEVELSDORF** (3): `DUEVELSDORF_GREEN1`, `DUEVELSDORF_GREY1`, `DUEVELSDORF_RED1`
**EINBOECK** (5): `EINBOECK_BLUE1`, `EINBOECK_GREEN1`, `EINBOECK_GREY`, `EINBOECK_RED1`, `EINBOECK_YELLOW1`
**ELHO** (1): `ELHO_ORANGE1`
**ELMERSMFG** (5): `ELMERSMFG_BEIGE1`, `ELMERSMFG_BLUE1`, `ELMERSMFG_GREY1`, `ELMERSMFG_ORANGE1`, `ELMERSMFG_RED`
**ERO** (3): `ERO_GREEN1`, `ERO_GREY1`, `ERO_RED1`
**EVERSAGRO** (3): `EVERSAGRO_BLACK`, `EVERSAGRO_GREY`, `EVERSAGRO_RED`
**FARESIN** (7): `FARESIN_BLUE1`, `FARESIN_BLUE2`, `FARESIN_GREEN1`, `FARESIN_GREY1`, `FARESIN_GREY2`, `FARESIN_RED1`, `FARESIN_WHITE`
**FARMAX** (1): `FARMAX_RED1`
**FARMET** (3): `FARMET_BLUE1`, `FARMET_BLUE2`, `FARMET_YELLOW1`
**FARMTECH** (4): `FARMTECH_GREEN1`, `FARMTECH_GREY1`, `FARMTECH_RED1`, `FARMTECH_YELLOW1`
**FENDT** (21): `FENDT_BIEGE1`, `FENDT_BLACK1`, `FENDT_BLACK2`, `FENDT_BLUE1`, `FENDT_BLUE2`, `FENDT_BRIGHTBLUE1`, `FENDT_BRIGHTGREEN`, `FENDT_DARKGREEN1`, `FENDT_DESIGN_GRILL`, `FENDT_GREY1`, `FENDT_GREY2`, `FENDT_GREY3`, `FENDT_GRILL`, `FENDT_NEWGREEN1`, `FENDT_OLDGREEN1`, `FENDT_ORANGE1`, `FENDT_RED1`, `FENDT_VIOLET1`, `FENDT_WHITE1`, `FENDT_WHITE2`, `FENDT_YELLOW1`
**FIAT** (7): `FIAT_BLACKPAINT`, `FIAT_BROWN`, `FIAT_GREENPAINT`, `FIAT_ORANGEPAINT`, `FIAT_RED`, `FIAT_WHITE`, `FIAT_WHITEPAINT`
**FLEXICOIL** (3): `FLEXICOIL_BLUEGRAY1`, `FLEXICOIL_DARKBLUEGREY1`, `FLEXICOIL_RED1`
**FLIEGL** (7): `FLIEGL_BLUE1`, `FLIEGL_GREEN1`, `FLIEGL_GREEN2`, `FLIEGL_GREEN3`, `FLIEGL_GREEN4`, `FLIEGL_GREY`, `FLIEGL_RED1`
**FORD** (1): `FORD_BLUE1`
**FORTSCHRITT** (4): `FORTSCHRITT_BLACK`, `FORTSCHRITT_BLUE`, `FORTSCHRITT_GREEN`, `FORTSCHRITT_RED`
**FORTUNA** (2): `FORTUNA_GREEN1`, `FORTUNA_GREY`
**FSI** (2): `FSI_GREEN1`, `FSI_RED1`
**GENERIC** (1): `GENERIC_CABLEMOUNT_GREEN`
**GERINGHOFF** (3): `GERINGHOFF_BLACK`, `GERINGHOFF_RED`, `GERINGHOFF_YELLOW`
**GESSNER** (11): `GESSNER_BLACK1`, `GESSNER_BLACK2`, `GESSNER_DARKGRAY1`, `GESSNER_GRAY1`, `GESSNER_GRAY2`, `GESSNER_GRAY3`, `GESSNER_GREEN1`, `GESSNER_GREEN2`, `GESSNER_ORANGE1`, `GESSNER_RED1`, `GESSNER_YELLOW1`
**GILIBERT** (2): `GILIBERT_RED1`, `GILIBERT_YELLOW1`
**GOEWEIL** (2): `GOEWEIL_BLUE1`, `GOEWEIL_YELLOW1`
**GOLDHOFER** (6): `GOLDHOFER_BLUE`, `GOLDHOFER_GREEN1`, `GOLDHOFER_GREEN2`, `GOLDHOFER_ORANGE1`, `GOLDHOFER_PINK1`, `GOLDHOFER_RED1`
**GORENC** (2): `GORENC_BLUE1`, `GORENC_RED1`
**GREATPLAINS** (2): `GREATPLAINS_BEIGE`, `GREATPLAINS_GREEN`
**GREGOIRE** (2): `GREGOIRE_GREEN1`, `GREGOIRE_ORANGE1`
**GREGOIREBESSON** (2): `GREGOIREBESSON_GRAY`, `GREGOIREBESSON_RED`
**GRIMME** (7): `GRIMME_BLACK`, `GRIMME_BLUE1`, `GRIMME_GREEN1`, `GRIMME_GREEN1_1`, `GRIMME_RED1`, `GRIMME_WHITE`, `GRIMME_YELLOW1`
**HARDI** (7): `HARDI_BEIGE`, `HARDI_BLUE`, `HARDI_GREEN`, `HARDI_GREY`, `HARDI_GREY2`, `HARDI_RED`, `HARDI_YELLOW`
**HATZENBICHLER** (7): `HATZENBICHLER_BLACK`, `HATZENBICHLER_DARKBLUE1`, `HATZENBICHLER_GREEN`, `HATZENBICHLER_GREY2`, `HATZENBICHLER_RED`, `HATZENBICHLER_YELLOW`, `HATZENBICHLER_YELLOW1`
**HAUER** (3): `HAUER_BLACK`, `HAUER_GREY1`, `HAUER_ORANGE`
**HAWE** (3): `HAWE_GREEN1`, `HAWE_GREY1`, `HAWE_RED1`
**HEIZOMAT** (4): `HEIZOMAT_DARKGREY`, `HEIZOMAT_GREEN`, `HEIZOMAT_GREY`, `HEIZOMAT_YELLOW`
**HELIANTHUS** (12): `HELIANTHUS_BLUE1`, `HELIANTHUS_BLUE_1`, `HELIANTHUS_BROWN_1`, `HELIANTHUS_GREEN1`, `HELIANTHUS_GREEN2`, `HELIANTHUS_GREEN3`, `HELIANTHUS_GREEN4`, `HELIANTHUS_GREEN5`, `HELIANTHUS_RED1`, `HELIANTHUS_RED2`, `HELIANTHUS_WHITE1`, `HELIANTHUS_YELLOW1`
**HOLARAS** (2): `HOLARAS_GREEN`, `HOLARAS_ORANGE`
**HOLMER** (9): `HOLMER_BLUE`, `HOLMER_BLUE_3`, `HOLMER_BLUE_4`, `HOLMER_GREEN1`, `HOLMER_GREY1`, `HOLMER_GREY2`, `HOLMER_ORANGE`, `HOLMER_RED1`, `HOLMER_YELLOW_1`
**HORSCH** (4): `HORSCH_BEIGE1`, `HORSCH_GREY1`, `HORSCH_GREY2`, `HORSCH_RED1`
**HUB** (2): `HUB_BOLT_DEFAULT`, `HUB_DEFAULT`
**HUERLIMANN** (21): `HUERLIMANN_BEIGE_1`, `HUERLIMANN_BEIGE_2`, `HUERLIMANN_BEIGE_3`, `HUERLIMANN_BEIGE_4`, `HUERLIMANN_BLUE_1`, `HUERLIMANN_BLUE_2`, `HUERLIMANN_BLUE_3`, `HUERLIMANN_BLUE_4`, `HUERLIMANN_BLUE_5`, `HUERLIMANN_BLUE_6`, `HUERLIMANN_GREEN1`, `HUERLIMANN_GREEN1_1`, `HUERLIMANN_GREEN1_2`, `HUERLIMANN_GREEN1_3`, `HUERLIMANN_ORANGE1`, `HUERLIMANN_ORANGE1_1`, `HUERLIMANN_RED1`, `HUERLIMANN_RED1_1`, `HUERLIMANN_RED1_2`, `HUERLIMANN_YELLOW_1`, `HUERLIMANN_YELLOW_2`
**HUSQVARNA** (4): `HUSQVARNA_BLUE1`, `HUSQVARNA_GREY2`, `HUSQVARNA_ORANGE1`, `HUSQVARNA_RED1`
**IMPEX** (1): `IMPEX_GREEN1`
**INTERNATIONAL** (11): `INTERNATIONAL_BEIGE1`, `INTERNATIONAL_BEIGE2`, `INTERNATIONAL_BEIGE3`, `INTERNATIONAL_BLACK1`, `INTERNATIONAL_BROWN1`, `INTERNATIONAL_BROWN2`, `INTERNATIONAL_GREY1`, `INTERNATIONAL_GREY2`, `INTERNATIONAL_GREY3`, `INTERNATIONAL_RED1`, `INTERNATIONAL_WHITE1`
**ISARIA** (1): `ISARIA_BLUE1`
**ISEKI** (4): `ISEKI_BLUE1`, `ISEKI_DARKBLUE1`, `ISEKI_ORANGE1`, `ISEKI_WHITE1`
**ITRUNNER** (12): `ITRUNNER_BLUE1`, `ITRUNNER_BLUE_1`, `ITRUNNER_BROWN_1`, `ITRUNNER_GREEN1`, `ITRUNNER_GREEN2`, `ITRUNNER_GREEN3`, `ITRUNNER_GREEN4`, `ITRUNNER_GREEN5`, `ITRUNNER_RED1`, `ITRUNNER_RED2`, `ITRUNNER_WHITE1`, `ITRUNNER_YELLOW1`
**JCB** (3): `JCB_ORANGE`, `JCB_RED_1`, `JCB_YELLOW1`
**JENZ** (3): `JENZ_GREEN1`, `JENZ_GREYRAL7043`, `JENZ_RED1`
**JMMANUFACTURING** (6): `JMMANUFACTURING_BLACK1`, `JMMANUFACTURING_BLUE1`, `JMMANUFACTURING_GREEN1`, `JMMANUFACTURING_RED1`, `JMMANUFACTURING_RED2`, `JMMANUFACTURING_YELLOW1`
**JOHNDEERE** (9): `JOHNDEERE_BLACK1`, `JOHNDEERE_BROWN1`, `JOHNDEERE_BROWN2`, `JOHNDEERE_BROWN3`, `JOHNDEERE_BROWN4`, `JOHNDEERE_GREEN1`, `JOHNDEERE_GREEN2`, `JOHNDEERE_ORANGE1`, `JOHNDEERE_YELLOW1`
**JONSERED** (2): `JONSERED_GREY2`, `JONSERED_RED1`
**JOSKIN** (3): `JOSKIN_GREEN1`, `JOSKIN_GREY`, `JOSKIN_YELLOW1`
**JUNGHEINRICH** (2): `JUNGHEINRICH_GREY1`, `JUNGHEINRICH_YELLOW1`
**KAERCHER** (5): `KAERCHER_GREY3`, `KAERCHER_GREY4`, `KAERCHER_RED`, `KAERCHER_YELLOW1`, `KAERCHER_YELLOW2`
**KAWECO** (4): `KAWECO_GREEN`, `KAWECO_GREEN1`, `KAWECO_GREY`, `KAWECO_ORANGE1`
**KEMPER** (3): `KEMPER_GREEN1`, `KEMPER_RED1`, `KEMPER_YELLOW_1`
**KESLA** (1): `KESLA_YELLOW1`
**KINZE** (7): `KINZE_BEIGE`, `KINZE_BLACK`, `KINZE_BLUE`, `KINZE_GREY1`, `KINZE_GREY2`, `KINZE_ORANGE1`, `KINZE_RED1`
**KIROVETS** (4): `KIROVETS_BLUE_1`, `KIROVETS_RED_1`, `KIROVETS_YELLOW_1`, `KIROVETS_YELLOW_2`
**KLINE** (1): `KLINE_GREEN1`
**KNOCHE** (1): `KNOCHE_RED1`
**KOECKERLING** (1): `KOECKERLING_BLUE1`
**KOLLER** (2): `KOLLER_RED1`, `KOLLER_YELLOW1`
**KOMATSU** (7): `KOMATSU_BLACK`, `KOMATSU_BLUE`, `KOMATSU_GREEN`, `KOMATSU_GREY`, `KOMATSU_REDMETAL`, `KOMATSU_REDPLASTIC`, `KOMATSU_YELLOW`
**KONGSKILDE** (1): `KONGSKILDE_RED`
**KOTTE** (9): `KOTTE_BLUE1`, `KOTTE_GREEN1`, `KOTTE_GREEN2`, `KOTTE_GREEN3`, `KOTTE_GREY1`, `KOTTE_GREY2`, `KOTTE_GREY3`, `KOTTE_RED1`, `KOTTE_YELLOW1`
**KRAMER** (4): `KRAMER_GREEN`, `KRAMER_GREY1`, `KRAMER_GREY2`, `KRAMER_RED`
**KRAMPE** (5): `KRAMPE_BLACK1`, `KRAMPE_GREEN1`, `KRAMPE_GREY1`, `KRAMPE_RED1`, `KRAMPE_WHITE1`
**KROEGER** (6): `KROEGER_BLACK2`, `KROEGER_GREEN1`, `KROEGER_GREY1`, `KROEGER_GREY2`, `KROEGER_RED1`, `KROEGER_YELLOW1`
**KRONE** (8): `KRONE_BLACK2`, `KRONE_BLUE5`, `KRONE_GREEN1`, `KRONE_GREY`, `KRONE_RED1`, `KRONE_YELLOW1`, `KRONE_YELLOW2`, `KRONE_YELLOW4`
**KUBOTA** (2): `KUBOTA_BLACK1`, `KUBOTA_ORANGE1`
**KUHN** (8): `KUHN_BLACK3`, `KUHN_BLUE1`, `KUHN_BLUE2`, `KUHN_GREY`, `KUHN_RED1`, `KUHN_RED2`, `KUHN_WHITE1`, `KUHN_YELLOW1`
**KVERNELAND** (5): `KVERNELAND_GREEN1`, `KVERNELAND_GREEN2`, `KVERNELAND_GREY1`, `KVERNELAND_GREY2`, `KVERNELAND_RED1`
**LACOTEC** (1): `LACOTEC_GREEN1`
**LANDINI** (6): `LANDINI_BLUE1`, `LANDINI_BLUE2`, `LANDINI_GREEN1`, `LANDINI_GREY1`, `LANDINI_GREY2`, `LANDINI_RED1`
**LELY** (3): `LELY_BEIGE1`, `LELY_COPPER`, `LELY_RED1`
**LEMKEN** (4): `LEMKEN_BLUE1`, `LEMKEN_GREY1`, `LEMKEN_GREY2`, `LEMKEN_RED1`
**LIEBHERR** (7): `LIEBHERR_BLACK2`, `LIEBHERR_BLUE1`, `LIEBHERR_BLUE2`, `LIEBHERR_GREY5`, `LIEBHERR_RED1`, `LIEBHERR_RED2`, `LIEBHERR_YELLOW1`
**LINDNER** (5): `LINDNER_BLACK`, `LINDNER_GREY1`, `LINDNER_RED1`, `LINDNER_WHITE1`, `LINDNER_WHITE2`
**LIZARD** (8): `LIZARD_BLUE1`, `LIZARD_BLUE2`, `LIZARD_BLUE3`, `LIZARD_ECRU1`, `LIZARD_OLIVE1`, `LIZARD_PINK1`, `LIZARD_PURPLE1`, `LIZARD_RED1`
**MACDON** (2): `MACDON_GREY`, `MACDON_RED`
**MACK** (1): `MACK_RED1`
**MAGSI** (2): `MAGSI_BLACK1`, `MAGSI_GREY`
**MAHINDRA** (2): `MAHINDRA_BLACK1`, `MAHINDRA_RED1`
**MAN** (15): `MAN_BEIGECLASSIC`, `MAN_BEIGE_1`, `MAN_BEIGE_2`, `MAN_BEIGE_3`, `MAN_BLUE1`, `MAN_BLUE2`, `MAN_BLUE3`, `MAN_BLUE4`, `MAN_BLUE5`, `MAN_BLUE6`, `MAN_GREEN_1`, `MAN_OLDGREEN`, `MAN_RED1`, `MAN_RED2`, `MAN_YELLOW_1`
**MANITOU** (11): `MANITOU_BEIGE`, `MANITOU_BLACK`, `MANITOU_BLUE`, `MANITOU_BRIGHTYELLOW`, `MANITOU_DARKGREY`, `MANITOU_GREY`, `MANITOU_GREY3`, `MANITOU_LIGHTGRAY`, `MANITOU_ORANGE`, `MANITOU_RED`, `MANITOU_WHITE`
**MARSHALL** (6): `MARSHALL_BLACK2`, `MARSHALL_BLUE1`, `MARSHALL_BROWN1`, `MARSHALL_BROWN2`, `MARSHALL_BROWN3`, `MARSHALL_RED1`
**MASSEYFERGUSON** (12): `MASSEYFERGUSON_BEIGE_1`, `MASSEYFERGUSON_DARK_GREY`, `MASSEYFERGUSON_DIAMOND_GREY`, `MASSEYFERGUSON_GREEN`, `MASSEYFERGUSON_GREY_1`, `MASSEYFERGUSON_GREY_4`, `MASSEYFERGUSON_GREY_5`, `MASSEYFERGUSON_LIGHT_GREY`, `MASSEYFERGUSON_ORANGE`, `MASSEYFERGUSON_RED`, `MASSEYFERGUSON_SILVER`, `MASSEYFERGUSON_WHITE`
**MCCORMACK** (2): `MCCORMACK_RED1`, `MCCORMACK_YELLOW1`
**MCCORMICK** (7): `MCCORMICK_BLACK1`, `MCCORMICK_GREY1`, `MCCORMICK_GREY2`, `MCCORMICK_GREY3`, `MCCORMICK_GREY4`, `MCCORMICK_RED1`, `MCCORMICK_RED2`
**MCCULLOCH** (3): `MCCULLOCH_GREY2`, `MCCULLOCH_RED1`, `MCCULLOCH_YELLOW1`
**MERCEDES** (25): `MERCEDES_TRAC_BEIGE`, `MERCEDES_TRAC_GREEN_DARK`, `MERCEDES_TRAC_GREEN_LIGHT`, `MERCEDES_TRAC_GREY`, `MERCEDES_TRAC_PURPLE`, `MERCEDES_TRAC_SILBERDISTEL_BRIGHT`, `MERCEDES_TRAC_SILBERDISTEL_DARK`, `MERCEDES_TRUCK_BLUE`, `MERCEDES_TRUCK_DARKCHROME`, `MERCEDES_TRUCK_DARKGREY`, `MERCEDES_TRUCK_DARKGREY2`, `MERCEDES_TRUCK_GREY`, `MERCEDES_TRUCK_GREY2`, `MERCEDES_TRUCK_INTERIOR_BEIGE`, `MERCEDES_TRUCK_LIGHTGREY`, `MERCEDES_TRUCK_RED`, `MERCEDES_TRUCK_WHITE`, `MERCEDES_UNIMOG_BRIGHTGREEN`, `MERCEDES_UNIMOG_DARKGREEN`, `MERCEDES_UNIMOG_DARKGREY`, `MERCEDES_UNIMOG_GREEN1`, `MERCEDES_UNIMOG_GREEN2`, `MERCEDES_UNIMOG_GREY`, `MERCEDES_UNIMOG_ORANGE`, `MERCEDES_UNIMOG_YELLOW`
**MERIDIAN** (4): `MERIDIAN_GREY1`, `MERIDIAN_RED`, `MERIDIAN_WHITE1`, `MERIDIAN_YELLOW`
**MERLO** (6): `MERLO_GREEN1`, `MERLO_GREY1`, `MERLO_GREY2`, `MERLO_GREY3`, `MERLO_GREY4`, `MERLO_WHITE1`
**METALTECH** (3): `METALTECH_GREEN`, `METALTECH_GREEN_1`, `METALTECH_RED`
**MONOSEM** (3): `MONOSEM_BLUE`, `MONOSEM_RED`, `MONOSEM_WHITE`
**MZURI** (2): `MZURI_GREY1`, `MZURI_ORANGE1`
**NEWHOLLAND** (12): `NEWHOLLAND_BLACK1`, `NEWHOLLAND_BLUE1`, `NEWHOLLAND_BLUE2`, `NEWHOLLAND_BLUE4`, `NEWHOLLAND_DARKBLUE1`, `NEWHOLLAND_GOLD1`, `NEWHOLLAND_GREY1`, `NEWHOLLAND_GREY2`, `NEWHOLLAND_ORANGE1`, `NEWHOLLAND_RED1`, `NEWHOLLAND_WHITE1`, `NEWHOLLAND_YELLOW1`
**NEXAT** (2): `NEXAT_BLACK`, `NEXAT_RED`
**NORDSTEN** (2): `NORDSTEN_BLUE1`, `NORDSTEN_ORANGE1`
**NOVAG** (3): `NOVAG_RED1`, `NOVAG_WHITE1`, `NOVAG_WHITE2`
**OLOFSFORS** (1): `OLOFSFORS_BLUE1`
**OXBO** (6): `OXBO_GREEN1`, `OXBO_GREY1`, `OXBO_GREY2`, `OXBO_GREY3`, `OXBO_WHITE1`, `OXBO_YELLOW1`
**PALADIN** (2): `PALADIN_GREY`, `PALADIN_RED`
**PALFINGER** (1): `PALFINGER_RED`
**PFANZELT** (4): `PFANZELT_GREY1`, `PFANZELT_GREY2`, `PFANZELT_SILVER1`, `PFANZELT_TURQOISE1`
**POETTINGER** (4): `POETTINGER_GREEN1`, `POETTINGER_RED1`, `POETTINGER_WHITE1`, `POETTINGER_YELLOW`
**PONSSE** (11): `PONSSE_BLACK1`, `PONSSE_BLACK2`, `PONSSE_BLUE1`, `PONSSE_BLUE2`, `PONSSE_BLUE3`, `PONSSE_GREY1`, `PONSSE_GREY2`, `PONSSE_GREY4`, `PONSSE_RED1`, `PONSSE_YELLOW1`, `PONSSE_YELLOW2`
**PORSCHEDIESEL** (4): `PORSCHEDIESEL_BEIGE1`, `PORSCHEDIESEL_BROWN1`, `PORSCHEDIESEL_RED1`, `PORSCHEDIESEL_YELLOW1`
**PRINOTH** (3): `PRINOTH_BLACK1`, `PRINOTH_GREY1`, `PRINOTH_RED1`
**PROVITIS** (1): `PROVITIS_ORANGE1`
**QUICKE** (2): `QUICKE_BLACK1`, `QUICKE_ORANGE1`
**RABE** (2): `RABE_BLACK1`, `RABE_BLUE1`
**RANDON** (3): `RANDON_ORANGE1`, `RANDON_ORANGE2`, `RANDON_RED1`
**REITER** (3): `REITER_GREY`, `REITER_RED`, `REITER_WHITE`
**RIEDLER** (1): `RIEDLER_GREY1`
**RIGITRAC** (4): `RIGITRAC_GREY`, `RIGITRAC_ORANGE1`, `RIGITRAC_RED1`, `RIGITRAC_YELLOW`
**RIM** (6): `RIM_ADDITIONAL_DEFAULT`, `RIM_BOLT_DEFAULT`, `RIM_CONFIGURATION_BLACK`, `RIM_CONFIGURATION_CHROME`, `RIM_CONFIGURATION_WHITE`, `RIM_DEFAULT`
**RISUTEC** (2): `RISUTEC_GREY1`, `RISUTEC_YELLOW1`
**ROPA** (7): `ROPA_BLACK1`, `ROPA_BLACK2`, `ROPA_BLUE`, `ROPA_DARKGRAY`, `ROPA_GRAY`, `ROPA_GRAY1`, `ROPA_YELLOW`
**ROSTSELMASH** (8): `ROSTSELMASH_BROWN1`, `ROSTSELMASH_GREEN1`, `ROSTSELMASH_ORANGE1`, `ROSTSELMASH_ORANGE2`, `ROSTSELMASH_PURPLE1`, `ROSTSELMASH_RED1`, `ROSTSELMASH_RED2`, `ROSTSELMASH_YELLOW1`
**ROTTNE** (4): `ROTTNE_BLUE1`, `ROTTNE_GREY1`, `ROTTNE_ORANGE1`, `ROTTNE_ORANGE2`
**RUDOLFHOERMANN** (14): `RUDOLFHOERMANN_BEIGE`, `RUDOLFHOERMANN_BLUE`, `RUDOLFHOERMANN_BROWN`, `RUDOLFHOERMANN_DARKBEIGE`, `RUDOLFHOERMANN_DARKGREY`, `RUDOLFHOERMANN_GREEN`, `RUDOLFHOERMANN_GREYALU`, `RUDOLFHOERMANN_LIGHTGREEN`, `RUDOLFHOERMANN_LIGHTGREY`, `RUDOLFHOERMANN_OXIDRED`, `RUDOLFHOERMANN_RED`, `RUDOLFHOERMANN_WHITEALU`, `RUDOLFHOERMANN_WOODBRIGHT`, `RUDOLFHOERMANN_WOODDARK`
**RUDOLPHSOHN** (4): `RUDOLPHSOHN_COVERGREEN`, `RUDOLPHSOHN_DARKGREEN`, `RUDOLPHSOHN_LIGHTGREEN`, `RUDOLPHSOHN_RED1`
**SALEK** (7): `SALEK_GREEN1`, `SALEK_GREEN2`, `SALEK_GREY1`, `SALEK_ORANGE1`, `SALEK_RED1`, `SALEK_RED2`, `SALEK_YELLOW1`
**SALFORD** (1): `SALFORD_RED1`
**SAMASZ** (4): `SAMASZ_BLACK`, `SAMASZ_GREEN`, `SAMASZ_ORANGE`, `SAMASZ_WHITE`
**SAME** (4): `SAME_BLACK1`, `SAME_BLACK2`, `SAME_GREY1`, `SAME_RED1`
**SAMPOROSENLEW** (4): `SAMPOROSENLEW_BLUE1`, `SAMPOROSENLEW_RED1`, `SAMPOROSENLEW_YELLOW1`, `SAMPOROSENLEW_YELLOW2`
**SAMSONAGRO** (3): `SAMSONAGRO_BLUE`, `SAMSONAGRO_GREEN`, `SAMSONAGRO_YELLOWPTO`
**SCHAEFFER** (6): `SCHAEFFER_BLUE1`, `SCHAEFFER_GREY1`, `SCHAEFFER_RED1`, `SCHAEFFER_SILVER`, `SCHAEFFER_YELLOW1`, `SCHAEFFER_YELLOW2`
**SCHOUTEN** (2): `SCHOUTEN_GREY1`, `SCHOUTEN_ORANGE1`
**SCHUITEMAKER** (4): `SCHUITEMAKER_BLACK`, `SCHUITEMAKER_GREY`, `SCHUITEMAKER_ORANGE1`, `SCHUITEMAKER_RED1`
**SCHWARZMUELLER** (4): `SCHWARZMUELLER_GREY1`, `SCHWARZMUELLER_ORANGE1`, `SCHWARZMUELLER_RED1`, `SCHWARZMUELLER_YELLOW1`
**SEEDHAWK** (3): `SEEDHAWK_RED1`, `SEEDHAWK_YELLOW1`, `SEEDHAWK_YELLOW2`
**SENNEBOGEN** (1): `SENNEBOGEN_GREEN1`
**SEPPKNUSEL** (3): `SEPPKNUSEL_GREY1`, `SEPPKNUSEL_RED1`, `SEPPKNUSEL_YELLOW1`
**SHARED** (43): `SHARED_BEIGE`, `SHARED_BLACK0`, `SHARED_BLACK1`, `SHARED_BLACK2`, `SHARED_BLACK3`, `SHARED_BLACK4`, `SHARED_BLACK5`, `SHARED_BLACK6`, `SHARED_BLACKJET`, `SHARED_BLACKONYX`, `SHARED_BLUE1`, `SHARED_BLUE2`, `SHARED_BLUE3`, `SHARED_BLUENAVY`, `SHARED_BROWN`, `SHARED_BROWN1`, `SHARED_BROWN2`, `SHARED_BROWN3`, `SHARED_DA_METAL_BLACK`, `SHARED_GLASS_ORANGE`, `SHARED_GLASS_RED`, `SHARED_GREY`, `SHARED_GREY1`, `SHARED_GREY2`, `SHARED_GREY3`, `SHARED_GREY4`, `SHARED_GREY5`, `SHARED_GREYDARK`, `SHARED_GREYLIGHT`, `SHARED_RED1`, `SHARED_REDCRIMSON`, `SHARED_SILVER`, `SHARED_SILVERROPE1`, `SHARED_SKIN1`, `SHARED_WHITE1`, `SHARED_WHITE2`, `SHARED_WRAP_BLACK`, `SHARED_WRAP_BLUE`, `SHARED_WRAP_GREEN`, `SHARED_WRAP_PINK`, `SHARED_WRAP_WHITE`, `SHARED_YELLOW1`, `SHARED_YELLOW2`
**SILOKING** (2): `SILOKING_BLUE1`, `SILOKING_RED1`
**SIP** (4): `SIP_BLUE1`, `SIP_GREY1`, `SIP_RED1`, `SIP_RED2`
**SKODA** (11): `SKODA_BLACK_MAGIC`, `SKODA_BRILLIANT_SILVER_METALLIC`, `SKODA_ENERGY_BLUE`, `SKODA_GOLD_BRONZE`, `SKODA_GRAPHITE_GREY_METALLIC`, `SKODA_MAMBA_GREEN`, `SKODA_MOON_WHITE`, `SKODA_PHOENIX_ORANGE_METALLIC`, `SKODA_RACE_BLUE_METALLIC`, `SKODA_STEEL_GREY`, `SKODA_VELVET_RED_METALLIC`
**STARA** (8): `STARA_BEIGE`, `STARA_BEIGE1`, `STARA_COLORED1`, `STARA_COLOYELLOW`, `STARA_GREEN`, `STARA_GREEN1`, `STARA_GREY`, `STARA_ORANGE`
**STARKINDUSTRIES** (3): `STARKINDUSTRIES_BLUE1`, `STARKINDUSTRIES_BLUE2`, `STARKINDUSTRIES_GREEN1`
**STEIGER** (1): `STEIGER_GREEN`
**STEMA** (2): `STEMA_GREY1`, `STEMA_RED1`
**STEPA** (3): `STEPA_GREY2`, `STEPA_RED1`, `STEPA_YELLOW1`
**STEYR** (7): `STEYR_BLACK`, `STEYR_GREY1`, `STEYR_GREY2`, `STEYR_ORANGE`, `STEYR_RED1`, `STEYR_WHITE1`, `STEYR_YELLOW1`
**STIHL** (5): `STIHL_BROWN`, `STIHL_GREY_1`, `STIHL_MAGENTA1`, `STIHL_ORANGE_1`, `STIHL_WHITE1`
**STOLL** (3): `STOLL_GREY1`, `STOLL_GREY2`, `STOLL_RED1`
**STRAUTMANN** (4): `STRAUTMANN_GREEN1`, `STRAUTMANN_GREY1`, `STRAUTMANN_RED1`, `STRAUTMANN_YELLOW1`
**SUER** (1): `SUER_GREY1`
**SUMMERSMFG** (2): `SUMMERSMFG_GREEN1`, `SUMMERSMFG_RED1`
**TAJFUN** (1): `TAJFUN_RED1`
**TATRA** (7): `TATRA_BEIGE1`, `TATRA_BEIGE2`, `TATRA_BEIGE3`, `TATRA_BLUE1`, `TATRA_ORANGE1`, `TATRA_ORANGE2`, `TATRA_RED1`
**THUERINGERAGRAR** (2): `THUERINGERAGRAR_RED1`, `THUERINGERAGRAR_YELLOW1`
**THUNDERCREEK** (5): `THUNDERCREEK_BLUE`, `THUNDERCREEK_GREEN1`, `THUNDERCREEK_GREY1`, `THUNDERCREEK_GREY2`, `THUNDERCREEK_RED1`
**TMCCANCELA** (2): `TMCCANCELA_GREY`, `TMCCANCELA_ORANGE`
**TREFFLER** (2): `TREFFLER_BLUE1`, `TREFFLER_YELLOW1`
**TRELLEBORG** (2): `TRELLEBORG_RED1`, `TRELLEBORG_WHITE3`
**UNIA** (2): `UNIA_GREY1`, `UNIA_RED1`
**UNVERFERTH** (9): `UNVERFERTH_BEIGE1`, `UNVERFERTH_BEIGE2`, `UNVERFERTH_BLACK1`, `UNVERFERTH_BLUE1`, `UNVERFERTH_GREEN`, `UNVERFERTH_GREEN2`, `UNVERFERTH_GREEN3`, `UNVERFERTH_RED1`, `UNVERFERTH_YELLOW1`
**UNVERFETH** (4): `UNVERFETH_BEIGE`, `UNVERFETH_GREY`, `UNVERFETH_RED`, `UNVERFETH_WHITE`
**VAEDERSTAD** (2): `VAEDERSTAD_RED1`, `VAEDERSTAD_YELLOW1`
**VALTRA** (21): `VALTRA_BEIGE`, `VALTRA_BLACK1`, `VALTRA_BLACK2`, `VALTRA_BLUE1`, `VALTRA_BLUE2`, `VALTRA_BLUE3`, `VALTRA_BLUE4`, `VALTRA_GOLD1`, `VALTRA_GREEN1`, `VALTRA_GREEN2`, `VALTRA_GREEN3`, `VALTRA_GREY1`, `VALTRA_GREY2`, `VALTRA_GREY3`, `VALTRA_OLIVE`, `VALTRA_ORANGE1`, `VALTRA_RED1`, `VALTRA_RED2`, `VALTRA_SPECIAL`, `VALTRA_WHITE`, `VALTRA_YELLOW1`
**VEENHUIS** (3): `VEENHUIS_GREY`, `VEENHUIS_ORANGE`, `VEENHUIS_RED`
**VERMEER** (1): `VERMEER_YELLOW`
**VERSATILE** (4): `VERSATILE_ORANGE1`, `VERSATILE_ORANGE2`, `VERSATILE_ORANGE3`, `VERSATILE_RED1`
**VERVAET** (7): `VERVAET_BEIGE`, `VERVAET_BLUE1`, `VERVAET_GREEN1`, `VERVAET_GREY`, `VERVAET_GREY1`, `VERVAET_RED1`, `VERVAET_WHITE`
**VICON** (3): `VICON_BEIGE`, `VICON_GREY1`, `VICON_RED1`
**VOGELNOOT** (2): `VOGELNOOT_GREEN1`, `VOGELNOOT_RED1`
**VOGELSANG** (4): `VOGELSANG_BLUE1`, `VOGELSANG_BRASS`, `VOGELSANG_GREEN`, `VOGELSANG_RED1`
**VOLVO** (11): `VOLVO_BLACK1`, `VOLVO_BM_GREEN1`, `VOLVO_BM_GREEN2`, `VOLVO_BM_RED1`, `VOLVO_BM_YELLOW1`, `VOLVO_GREEN1`, `VOLVO_GREY1`, `VOLVO_ORANGE1`, `VOLVO_PURPLE1`, `VOLVO_RED1`, `VOLVO_YELLOW1`
**VREDO** (2): `VREDO_ORANGE`, `VREDO_RED`
**WALKABOUT** (2): `WALKABOUT_BLUE1`, `WALKABOUT_WHITE1`
**WALTERSCHEID** (3): `WALTERSCHEID_BLACK1`, `WALTERSCHEID_YELLOW1`, `WALTERSCHEID_YELLOW2`
**WARZEE** (3): `WARZEE_LOGOBLUE`, `WARZEE_LOGOGRAY`, `WARZEE_YELLOW`
**WEBERMT** (1): `WEBERMT_BLUE1`
**WEIDEMANN** (2): `WEIDEMANN_GREY`, `WEIDEMANN_RED`
**WELGER** (4): `WELGER_GREEN1`, `WELGER_GREEN2`, `WELGER_RED1`, `WELGER_YELLOW1`
**WESTTECH** (1): `WESTTECH_ORANGE1`
**WIENHOFF** (6): `WIENHOFF_BROWN`, `WIENHOFF_GOLD`, `WIENHOFF_GREEN`, `WIENHOFF_GREY`, `WIENHOFF_RED1`, `WIENHOFF_RED2`
**WIFO** (2): `WIFO_GREY`, `WIFO_RED`
**WILSONTRAILER** (1): `WILSONTRAILER_WHITE1`
**WOODMIZER** (1): `WOODMIZER_ORANGE1`
**ZETOR** (9): `ZETOR_BLUE2`, `ZETOR_BLUE3`, `ZETOR_BROWN_1`, `ZETOR_GREEN1`, `ZETOR_GREEN2`, `ZETOR_ORANGE1`, `ZETOR_RED1`, `ZETOR_YELLOW1`, `ZETOR_YELLOW2`
**ZIEGLER** (2): `ZIEGLER_RED`, `ZIEGLER_YELLOW`
**ZUNHAMMER** (9): `ZUNHAMMER_BLUE`, `ZUNHAMMER_GREEN1`, `ZUNHAMMER_GREEN3`, `ZUNHAMMER_GREY`, `ZUNHAMMER_RED1`, `ZUNHAMMER_RED2`, `ZUNHAMMER_YELLOW1`, `ZUNHAMMER_YELLOW2`, `ZUNHAMMER_YELLOW3`

</details>

---

## Caveats & methodology

- **Extensibility:** Part 2 sets are the base-game + unpacked-DLC baseline. Any installed **map** or **mod** can register additional `fillType`, `fruitType`, `sprayType`, `jointType`, `brand`, `inputAction`, `effectClass`, etc. at load time. Always treat these as "valid unless the active modset adds more."
- **Case sensitivity:** `fillType`/`sprayType`/`fillTypeCategory`/`densityMapHeightType` are UPPERCASE and matched as written. `fruitType` and `rigidBodyType` are normalized, so case doesn't matter. `jointType`/`workAreaType`/`particleType`/connection-hose names are lowercase/camelCase as written.
- **`effectClass` is an open set** resolved by class name at load — not a fixed registry.
- **`materialSlotName` is intentionally omitted as an enum** — it's per-model, not a registry.
- All Part 2 values were extracted directly from the cited source files and cross-checked against actual usage in `data/vehicles/**`, not transcribed by hand.
