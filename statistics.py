import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("test_outputs.csv")


faces = df["gender_scores_fair"].values



male = 0 
female = 0
not_confident = 0

for face in faces:
    face = face.strip("[").strip("]").split()
    M = float(face[0])
    F = float(face[1])
    if M >= 0.6:
        male += 1
    elif F >=0.6:
        female += 1
    else:
        not_confident+=1


# total = df['gender'].shape[0]
# male = df['gender'].value_counts()['Male']
# female =  total - male

total = male + female
print(f"not confident face: {not_confident}")
print(f"total number of faces: {total}")

print(f"the number of males: {male}. which is {(male/total)*100:.2f}%")
print(f"the number of males: {female}. which is {(female/total)*100:.2f}%")

fig = plt.figure(figsize = (10, 5))
plt.bar(['Males', 'Females'], [male, female], color ='maroon', width = 0.4)

plt.xlabel("gender")
plt.ylabel("number")
plt.title("gender representation")
plt.show()