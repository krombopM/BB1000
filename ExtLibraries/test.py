sp.run('cat 3IE9.pdb | grep "^HETATM" > hetatm.csv', shell=True)
linesToBeWritten = []
with open("hetatm.csv", "r") as f:
    for line in f:
        linesToBeWritten.append(" ".join(line.split()).replace(" ", ",") + "\n")
linesToBeWritten.insert(0, "hetatm,a,b,c,d,e,x,y,z,f,g,h\n")
with open("hetatm.csv", "w") as f:
    for item in linesToBeWritten:
        f.write(item)
df_other = pd.read_csv("out_top1000.csv")
hetatmX = df_other["x"].values.tolist()
hetatmY = df_other["y"].values.tolist()
hetatmZ = df_other["z"].values.tolist()
