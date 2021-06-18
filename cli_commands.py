import subprocess
print("Got subprocess import.")

def test_gcode(output):
    # run a test slicing program
    # app (containing the python app) is the directory when run
    print("Running slicer.")
    subprocess.run("cd .. && cd ./ZengerEngine/build && "
        "./CuraEngine slice -p -j /app/ZengerEngine-Presets/definitions/fdmprinter.def.json -j /app/ZengerEngine-Presets/definitions/creality_ender3.def.json -l /app/Test-STLs/5mm_Cube.stl -o " + output
        , shell=True)
    print("Ran test gcode.")