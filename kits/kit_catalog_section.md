## Kit Catalog

Browse available evaluation boards in `kits/`. See [kits/kits_catalog.md](kits/kits_catalog.md) for the complete table.

### Easy (Entry-Level)

Non-isolated DC/DC and low-power offline boards.

- **TPS62932EVM** · buck synchronous, 3.8-30 V → 3.3 / 5 V @ ~2 A, ~10 W
- **TPS563212EVM** · buck synchronous, 4.2-18 V → 3.3 V @ 3 A, ~10 W
- **TPS6213xEVM** · buck synchronous, 3-17 V → 3.3 / 5 V @ 3-4 A, ~15 W
- **STEVAL-VP12201F** · flyback, 85-265 VAC → 12 V @ 5 W, 5 W
- **STEVAL-ISA201V1** · buck (l5987), up to 24-25 V → 5 V @ 3 A, ~15 W
- **NCP1060FLBKGEVB** · flyback, 85-265 VAC → 12 V @ 0.6 A, ~7 W
- **NCP1076FLBKGEVB** · flyback, 85-265 VAC → 12 V @ 1.2 A, ~18 W
- **BD7F100EFJ-EVK-001** · flyback, 24 V DC → 5 V @ 0.8 A, 4 W
- **2190** · buck-boost, 3-12 V → 5 V USB, 2.5-5 W
- **EVAL_5BR2280BZ_700MA1** · high-voltage buck (non-isolated), 85-264 VAC input (for internals) -> DC bus high voltage? (Refer doc) → 15 V @ 0.7 A (~10.5 W) typical, ~10 W
- **DC2781A (LT8316 non-isolated buck demo)** · non-isolated buck (quasi-resonant boundary mode), 19-600 V DC input range → 12 V @ up to 200 mA, ~2.4 W
- **BM2P141X-EVK-001 (non-isolation buck converter)** · non-isolated buck (pwm current mode), 12-15 V (drain max 650 V but EVK is low power) → 14 V (10 W output), ~10 W

### Medium

Intermediate power, more complex control or wide-VIN.

- **[TPS23753AEVM-004](kits/ti_tps23753aevm_004/)** · poe flyback, 37-57 V (PoE) → 3.3 / 5 / 12 V (configurable), ~10 W
- **UCC28740EVM-525** · flyback dcm, 85-265 VAC → 5 V @ 2.1 A, 10 W
- **LM5118EVAL** · buck-boost, 5-75 V → 12 V @ 3 A, ~36 W
- **LM5176EVM-HP** · buck-boost synchronous, 6-36 V → 12 V @ 12 A, ~144 W
- **LM5576EVAL** · buck, 6-75 V → 5 V @ 3 A, ~15 W
- **EVLSTACF01-65WU** · active-clamp flyback (acf), 90-264 VAC → 5-20 V (USB-PD), 65 W
- **STEVAL-QUADV01** · multi-output buck + ldo, 3.5-38 / 60 V → multiple rails (A, B, C, LDO), ~10-20 W
- **EVAL_5BR2280BZ_700MA1** · high-voltage buck, 85-264 VAC → 15 V @ 0.7 A, 10.5 W
- **Si34061-KIT** · poe flyback, PoE 37-57 V → 12 V, ~25-30 W
- **EVQ3369-R-01A** · boost led driver, 4.5-36 V → LED strings (multi-channel), ~10-20 W
- **LM5146-Q1-EVM12V** · synchronous buck, 15-85 V → 12 V (adjustable 8-15 V), ~12 V x up to ~8 A = ~96 W
- **TPS55287-Q1EVM-085** · buck-boost synchronous, 3-36 V → 0.8-22 V (programmable), Up to 2 A output current (~ up to ~44 W at 22 V)

### Advanced / High Power

kW-class boards with complex topologies (LLC, PSFB, bidirectional, PFC+LLC).

- **STEVAL-DPSLLCK1** · llc full-bridge, DC bus 350-400 V → 3 kW @ low-V, 3000 W
- **EVAL_3KW_50V_PSU** · pfc + llc, 178-275 VAC → 50 V DC, 3000 W
- **REF-1KW-PSU-5G-SIC** · totem-pole pfc + hb-llc, mains AC → 48-54 V, 1000 W
- **EVAL_1K6W_PSU_CFD7_QD** · pfc + llc, mains AC → 12 / 48 V, 1600 W
- **EVAL_3K3W_BIDI_PSFB** · bidirectional psfb, HV bus <-> 54 V → Bidirectional, 3300 W
- **LMG1210EVM-012** · half-bridge gan stage, up to 300 V DC bus → configurable, 10-100+ W (by design)

> **Note:** Not all kits have folders yet. Contributions welcome! Use [`KIT_README_TEMPLATE.md`](templates/KIT_README_TEMPLATE.md) to add one.
