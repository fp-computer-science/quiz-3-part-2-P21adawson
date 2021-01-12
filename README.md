<h1 align="center">
    Fairfield College Preparatory School<br>
    Computer Programming - Mr. Mesquita<br>
    Quiz 3 - Part 2
</h1>

<h2 align="center">Due before 10:35 AM on 1/12 (25 pts.)</h2>

### Answer each of the following questions in a separate Python file named `quiz_3-#.py` where `#` is the number of the question. In your heading, put your name and the date you began working on the file. Each question will be worth 8 points.

---

<h3 align="center">A long time ago in a galaxy far, far away...</h3>

2. The Jedi Council has received two lists, one containing the names of new younglings, and the other containing their respective races. Master Yoda needs the lists combined so that they can be easily intrepreted by the Council. Write a program that contains a function which takes these two lists as parameters. The youngling's name and their races should be added to a list, and this list added to a larger list that the function returns and the program prints.

   <ins>Inputs</ins>
   ```python
   younglings = ['Petro', 'Katooni', 'Byph', 'Ganodi', 'Zatt', 'Gungi']
   race = ['Human', 'Tholothian', 'Ithorian', 'Rodian', 'Nautolan', 'Wookie']
   ```

   <ins>Output</ins>
   ```
   [['Petro', 'Human'], ['Katooni', 'Tholothian'], ['Byph', 'Ithorian'], ['Ganodi', 'Rodian'], ['Zatt', 'Nautolan'], ['Gungi', 'Wookie']]
   ```

3. In the Outer Rim territories, podracing is a favorite passtime. As with many sporting events, betting on the winner is also part of the experience. The droid that manages the collection of credits and who they are being placed on generates a report with all this information before the race begins. The report can be difficult for less sophisticated lifeforms to intrepret. Write a program that contains a function which take the compound list and returns 2 separate lists, one of the racers names, and another of the bets that were placed on them.
   
   <ins>Input</ins>
   ```python
   ledger = [['Sebulba', 100, 200, 400], ['Skywalker', 500, 100, 20000], ['Reeso', 200, 700, 100]]
   ```

   <ins>Output</ins>
   ```
   (['Sebulba', 'Skywalker', 'Reeso'], [100, 200, 400, 500, 100, 20000, 200, 700, 100])
   ```

4. The clone factory on the planet Kamino is responsible for making clone troopers for the Grand Army of the Republic. Though they possess the biomedical expertise to create clone troopers, they do not have a way to automatically assign numbers to each new trooper. Write a program that contains a function that assignes a number to a clone as it is created. The function should first select a random number between `0` and `9999`, and then add leading zeroes to the number as appropriate so the number is 4 digits long. The function should return this number and `CT-` should preceed it to create the clone's name. The program should prompt the user to input `Y` to generate a new name and `N` to stop. When the program stops, it should display a list of all the clone names generated.

   <ins>Sample Run</ins>
   ```
   Name a clone? Y
   New clone trooper name: CT-5555
   Name a clone? Y
   New clone trooper name: CT-0137
   Name a clone? y
   New clone trooper name: CT-0099
   Name a clone? y
   New clone trooper name: CT-0008
   Name a clone? N
   ['CT-5555', 'CT-0137', 'CT-0099', 'CT-0008']
   ```

<p align="center">Be sure to commit your code before the end of class. Only the latest commit will be graded.</p>
