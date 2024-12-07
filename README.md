# EnderLab

Tranform your 3D printer into a lab engine

## About this repo

* Enderlab
    * data : Json file for building Layout & Protocols
    * layout : Layout & Modules logic
    * scripts : Python scripts to help building data (json files)
    * action : Perform actions to execute protocols
    * printer : Transfert actions into printer commands

## Installation

Run `poetry install`

## Usage

```py
poetry install
poetry shell

python main.py
```

## License

Enderlab licensed under [Dual License v1.0](https://codis.tech/efcorebulk) (cFOSS: conditionallyFree OSS as a solution to OpenSource funding).

If you do not meet criteria for free usage of software with community license then you have to buy commercial one.
If eligible for free usage but still need active support: please contact assematpierrecpe@gmail.com

## TODO

- [ ] 2 Validation layout disposition (static : grid, variable : protocol)
- [ ] Make protocol independent of the layout, and be able to create a protocol from protocol reference and a layout. By making a matching between abstract wells <-> (module & well). Add layout validation
- [ ] Allow fake protocol running to "test & validate" protocol before real running
- [ ] GUI python / Web UI 
- Add extra data on wells : compounds: { "element_name": "concentration" } + Compute calculations about each concentration at any times in protocol
- Add function to manually set the origin (0.0)