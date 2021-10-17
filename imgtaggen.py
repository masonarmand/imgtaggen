#   ___                __    _                                 
#  / (_)_ __ ___   __ _\ \  | |_ __ _  __ _    __ _  ___ _ __  
# / /| | '_ ` _ \ / _` |\ \ | __/ _` |/ _` |  / _` |/ _ \ '_ \ 
# \ \| | | | | | | (_| |/ / | || (_| | (_| | | (_| |  __/ | | |
#  \_\_|_| |_| |_|\__, /_/   \__\__,_|\__, |  \__, |\___|_| |_|
#                 |___/               |___/   |___/           
#
# A very simple but useful script for generating huge lists of <img> tags 



import os

# text file containing tags
txt = '_tags.txt'

# tuple containing file types/extensions
imageTypes = ('.png', '.gif', '.jpeg', '.jpg', '.PNG', '.GIF', '.JPEG', '.JPG')

def main():
	# look through current directory
	for root, dirs, files in os.walk(r'.'):

		# check for files
		for file in files:

			# check to see if the file is an image file type
			if file.endswith(imageTypes):

				print(f'Adding {file} to {txt}')

				# open file "tags.txt" for writing and add the <img> tag to it
				f = open(txt, "a")
				f.write(f'<img src="{file}">\n')
				f.close()

if __name__ == "__main__":
	main()
