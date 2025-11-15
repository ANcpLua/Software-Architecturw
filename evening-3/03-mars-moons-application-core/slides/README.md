# Exercise Slides - Mars02

This folder contains the exercise slides for **Mars02: A Very Small Application Core**.

## Slide Images

1. `slide_mars02_01.png` - Mars: The Project Description
   - Shows the two moons Deimos and Phobos
   - Explains joint visibility requirement for measurements

2. `slide_mars02_02.png` - Mars: The Project Description / 2
   - Need for both moons to be visible as gravitational lenses
   - Software function Moon to calculate overlap minutes

3. `slide_mars02_03.png` - Mars: Assumptions
   - AS1: Mars day (sol) = 88775 earth seconds
   - Dividing into 25 mars hours, 100 mars minutes per hour

4. `slide_mars02_04.png` - Mars: Assumptions / 2
   - AS2: Mars-timestamps and Mars-intervals
   - AS3: Intervals can span to next day
   - AS4: Moons rise/set exactly in middle of Mars-minute

5. `slide_mars02_05.png` - Mars: Assumptions / 3
   - AS5: Intervals valid across consecutive days
   - AS6: Moon called by NASA experiment coordination software

6. `slide_mars02_06.png` - Mars: Requirements
   - REQ1: Input two Mars-intervals (Deimos, Phobos)
   - REQ2: Output overlap in Mars-minutes
   - REQ3: Twilight rule (1 minute if only one point in common)
   - REQ4: Human-computer interface for Earth testing

7. `slide_mars02_07.png` - Mars: An Example
   - Deimos (14:00, 22:40), Phobos (15:88, 22:07)
   - Result: 619 minutes overlap

8. `slide_mars02_08.png` - Mars: Another Example
   - Deimos (14:00, 22:40), Phobos (10:20, 22:07)
   - Result: 807 minutes overlap

9. `slide_mars02_09.png` - Mars: Yet Another Example
   - Deimos (18:55, 4:97), Phobos (10:39, 4:00)
   - Result: 1045 minutes overlap

10. `slide_mars02_10.png` - Mars: Twilight Rule Example
    - Deimos (18:55, 3:97), Phobos (10:39, 18:55)
    - Result: 1 minute (twilight rule applied)

## Exercise Context

**Exercise ID:** Mars02
**Evening:** 3
**Type:** Home
**PDF:** Pages 222-224 in Architecture Development slides

**Task:** Design a 4-component architecture for calculating joint visibility of Mars moons Deimos and Phobos.

**Components:**
- A: Parser (8 integers → structured windows)
- B: Normalizer (windows → Mars-minute intervals)
- C: Overlap Calculator (intervals → overlap duration)
- D: Duration Extractor (apply twilight rule)
