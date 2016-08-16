# How to set up 
0. Before running the program, get your data files ready frist. Merge all the files in the folder to a single file, using command line.
    - On Windows: http://www.wikihow.com/Merge-Text-(.Txt)-Files-in-Command-Prompt
    - On Linux/Mac: 
        ```sh
        cat * > 0828.txt
        ```

1. Install python.
    - On Windows: http://www.cnblogs.com/windinsky/archive/2012/09/20/2695520.html (Till Step 5)
    - On Mac: python is initially installed.
  
2. Make sure the folder `result` exsits in side of the folder `CarTesting`. If not, manually create one. 
  **Note**: You may also want to copy your data file (the file after merging) to the folder `CarTesting` and don't forget to update the path of the file in line 16 in `DataProcessing.py`. Normally it should be `./merged_file_name_here.txt`.
  
3. Run DataProcessing.py by command in terminal:
    ```sh  
    python DataProcessing.py
    ```
  
4. If no error comes up, you can find your output files in the folder `result`