import tensorflow as tf
from tensorflow import keras
from keras.models import load_model


generator = load_model("Generator_model_fair")
number_of_images = 150 

random_latent_vectors = tf.random.normal(shape=(number_of_images, 128))
generated_images = generator(random_latent_vectors)
generated_images *= 255
generated_images.numpy()


for i in range(number_of_images):
    img = keras.preprocessing.image.array_to_img(generated_images[i])
    img.save(f"fresh_images/generated_img_{i}.png")


print("Job finished")