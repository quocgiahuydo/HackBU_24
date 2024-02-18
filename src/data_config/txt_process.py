


class Txt_Process:
    def __init__(self,input_file, output_file):
        try:
            with open(input_file, 'r') as file:
                lines = file.readlines()
            
            keywords_to_remove = ['contains', '=', ':',",","!","$",".","IQ"]
            lines = [line.strip() for line in lines if line.strip() != '' and not any(keyword in line.lower() for keyword in keywords_to_remove)]


            with open(output_file, 'w') as file:
                file.write('\n'.join(lines))
            
            print(f"Processing complete. Filtered content saved to {output_file}")

        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


text = Txt_Process("food_menus/c4.txt","food_menus/c4_out.txt")