from tqdm import tqdm
import tensorflow as tf
import inception
import os

def run(directory):
  divided_path = os.path.join(directory, 'divided')

  with open(os.path.join(directory,'features.csv'), 'w') as file:
    with tf.Session() as sess:
      for img_name in tqdm(os.listdir(divided_path),'classifing images..'):
        process(divided_path, img_name, sess, file)

def process(divided_path, img_name, sess, file):    
  path = os.path.join(divided_path, img_name)
  results =  inception.classify_image(path,sess)
  write_file(img_name, results, file)

def write_file(img_name, results, file):
  output = img_name[:-4]    
  for r in results:
    output += ';'+r[0]+';'+str(r[1])
  output += '\n'       
  file.write(output)