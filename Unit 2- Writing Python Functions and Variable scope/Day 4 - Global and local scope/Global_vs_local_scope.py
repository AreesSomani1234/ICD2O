global_book = "Encyclopedia of Science" #global_book is declared outside al functions
                                        #Exists everywhere

def section_book():
    local_book = "Chemistry Handbook"
    print(f"In the section: We have the {global_book} and the {local_book}")

section_book()

print(f"In the library: We still have our trusty {global_book}")

# Attempting to use the local_book variable here would result in an error.
print(f"In the library: but not the ")
                   #            {^local_book}


