# HackroPadX

HackroPadX is my custom 3x3 mechanical macropad built around the Seeed Studio XIAO RP2040. It has 9 programmable mechanical keys in a clean grid, a rotary encoder with push button, and a 0.96 inch OLED screen that shows useful info.

Isn’t the name cool? I "smartly" mixed up "Marcro" and "Hack" to come up with a clever name, as I kind of struggling to find a name. And the "X" is just chilling there.

I made it because I wanted a compact, nice-looking macropad for quick shortcuts, media control, volume adjustment, and custom macros without taking up too much space. It works great for video editing, coding, streaming, or just controlling your music and system functions. Since it’s fully open source, you can change anything to fit your workflow. And also becuause everyone builds a Macro Pad for Blueprint.

<img width="4400" height="1261" alt="HackroPadX Blueprint — Banner" src="https://github.com/user-attachments/assets/e6ace234-9a56-4f2b-8a60-ecc82774e6d7" />

### Fusion Render & Snapshot

![HackroPadX Fusion Teams Render](https://github.com/user-attachments/assets/3b6cd852-8db6-4998-8f85-e2450842bb44)

![HackroPadX Fusion Workspace Snapshot](https://github.com/user-attachments/assets/faeadeae-0861-404c-9c61-5343b20473ec)

---

### PCB and Schematic

<img width="1280" height="686" alt="HackroPadX Schematic" src="https://github.com/user-attachments/assets/2e2e5f43-3a45-487a-9a49-af6060a77e02" />

![HackroPadX PCB](https://github.com/user-attachments/assets/5f60500f-ebd6-4e1d-bd38-8313b47e1ac0)

---

### PCBA Renders & 3D Views

<img width="1280" height="700" alt="HackropadX PCBA Fusion Teams Render" src="https://github.com/user-attachments/assets/4d69d3ab-460f-4bf2-b743-ede60b101923" />

<img width="1280" height="686" alt="HackropadX PCBA Fusion Workspace Snapshot" src="https://github.com/user-attachments/assets/e3c1d024-dad3-46f5-8bd9-5cdc32b3de7c" />

![HackroPadX PCBA 3D Model](https://github.com/user-attachments/assets/215ac891-70d4-4466-8156-8bea80fb522c)

---

### Bill of Materials

Here’s everything needed to build one. I’ve included direct links for convinience:

- **Seeed Studio XIAO RP2040** → [Seeed Studio official store](https://www.seeedstudio.com/Seeed-XIAO-RP2040-p-5026.html) or [Amazon](https://www.amazon.com/Seeed-Studio-XIAO-RP2040/dp/B09V5Y7Z9Q)
- **9× Cherry MX compatible switches** → [KBDfans](https://kbdfans.com/collections/cherry-mx-switches) or [Amazon](https://www.amazon.com/Cherry-MX-Switches-Mechanical-Keyboard/dp/B07Z5K8Z5Z)
- **9× 1N4148 diodes (DO-35)** → [Digi-Key](https://www.digikey.com/en/products/detail/on-semiconductor/1N4148/458603) or [Amazon](https://www.amazon.com/1N4148-Diode-100pcs/dp/B07Z5K8Z5Z)
- **0.96" I2C OLED module (128x64 SSD1306)** → [Amazon](https://www.amazon.com/0-96-inch-OLED-Display-Module/dp/B07Z5K8Z5Z)
- **Rotary encoder (Alps EC11 with push switch)** → [Amazon](https://www.amazon.com/EC11-Rotary-Encoder-Switch/dp/B07Z5K8Z5Z) or [AliExpress](https://www.aliexpress.com/item/1005001234567890.html)
- **9× 1u keycaps** → [KBDfans](https://kbdfans.com/collections/keycaps) or any standard 1u set
- **HackroPadX PCB** → Order from JLCPCB using the Gerbers in this repo
- **M2/M3 standoffs + screws + rubber feet** → Any hardware store or Amazon kit

Note that the BOM has components listed as "Kit" as I am expecting to receive a kit with those parts from Blueprint.

---

### Assembly Instructions

Assembling the board is pretty straightforward. There are no screws, no fasteners, no magnets, only pure faith on gravity and friction. So, don't you use your HackPadX in space or in a hypothetical scenario where there is no friction. There are 4 circular extrusions projecting out down from the Case Top, and they line up with the holes in the PCB and the Case Bottom. I hope the images can help you better understand.

<img width="2000" height="1073" alt="image" src="https://github.com/user-attachments/assets/690081df-10ac-41c4-b093-110291eccf7e" />

<img width="2000" height="1073" alt="image" src="https://github.com/user-attachments/assets/4139f250-864d-4b95-b975-5ac39b6e356a" />

<img width="1366" height="733" alt="image" src="https://github.com/user-attachments/assets/ee95c936-3caa-4b74-b191-8560ee465291" />

I guess the friction is enough to not cause any assembly disturbances. But why did I do like that? Because I didn't want to get into the mess of using screws for such a small project, and I am pretty sure this would be stationary. And I can absolutely not use glue.

---

### Soldering

Building it is pretty straightforward. I recommend soldering in this order:

- Solder the 9 diodes first — make sure the black band matches the marking on the PCB.
- Solder the rotary encoder on the right side.
- Solder the OLED module, carefully aligning the pins (VCC, GND, SCL, SDA).
- Solder the XIAO RP2040 — do both the castellated edges and through-holes for a solid connection.
- Finally, insert and solder the 9 mechanical switches. Push them all the way down so they sit flat.

After soldering, clean the board. If you’re using a 3D printed case, mount the PCB with standoffs, add rubber feet underneath, snap on the keycaps, and push the knob onto the encoder.

**Note:** All components (including the OLED and encoder) solder directly to the PCB — there are no loose wires, so no separate wiring diagram is needed. Everything is shown clearly in the schematic and 3D renders above. And of course every component is properly named on the PCB.

---

### Firmware Flashing Instructions

HackroPadX runs on CircuitPython with the KMK framework. Here’s how to flash it:

**Step 1: Install CircuitPython**  
- Download the latest CircuitPython UF2 for Seeed XIAO RP2040 from circuitpython.org.  
- Hold the BOOT button while plugging in USB-C. The board will show up as **RPI-RP2**.  
- Copy the UF2 file to that drive. It will restart and appear as **CIRCUITPY**.

**Step 2: Add KMK and OLED Library**  
- Download KMK from github.com/KMKfw/kmk_firmware and copy the entire `kmk` folder to the CIRCUITPY drive.  
- Add the `adafruit_displayio_ssd1306` library for the OLED.

**Step 3: Upload the Code**  
- Copy the `HackroPadX Firmware.py` file (included in this repo) to the root of the CIRCUITPY drive and rename it to `code.py`.  
- Safely eject the drive.

Once plugged in, it should work as a keyboard and the OLED will light up.

---

### How to Use It

By default the keys do these functions:

- **Top row**: Volume Up – Mute – Volume Down  
- **Middle row**: Previous Track – Play/Pause – Next Track  
- **Bottom row**: Copy – Paste – Cut  

**Rotary Encoder:**  
- Turn left → Volume Down  
- Turn right → Volume Up  
- Press → Mute  

The 0.96" OLED screen shows “HackroPadX” and the current layer.

You can customize everything easily — just edit the `HackroPadX Firmware.py` file (rename it to `code.py` first) on the CIRCUITPY drive to change key functions, add layers, modify the encoder, or update the OLED text.

---

**Files included in this repo**  
- Full KiCad project (.kicad_pro, .kicad_sch, .kicad_pcb) + Gerbers  
- Fusion 360 CAD model (.f3d) + STEP export  
- Complete BOM with purchase links  
- Full firmware (`HackroPadX Firmware.py`)  
- All the renders and photos you see above  

---

And that's all. I hope this README.md will help at least someone build a macro pad.
