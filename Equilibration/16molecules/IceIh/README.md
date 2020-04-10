You can run this simulation with the command:
```
lmp_machine < start.lmp
```
where ```lmp_machine``` is your lammps executable.

Notice that the simulation was performed with an anisotropic barostat to determine the equilibrium box size.
The file ```data.final``` is a lammps data file with the final configuration of the simulation.
Inside that file, the box size has been changed manually to the average value of Lx, Ly, and Lz calculated from the simulation.
