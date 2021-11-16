# time-dimension-SAD-DSS
Exercise about time dimension in DSS

#### Step by Step

1- Execute Sql in ```time-dimension-Sad-DSS/SQLQuery.sql```.

-- if you want build project, execute ```python .\setup.py build```

2- Create archive in .exe folder, with ```url.txt``` name.

3- Edit your connection string. This is a tutorial, how to create your string connection https://docs.microsoft.com/pt-br/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15

3.1- In the archive, put your string in this format ```Driver={SQL Server};Server=DESKTOP-7S8FN3H;Database=sad_test;trusted_connection=true;UID=sa;```, the program will read just one line.

#### Example

Input ```16/11/2021```

Input ```20/12/2021```

Input ```y```

Input ```21/12/2021```

Input ```06/01/2022```

Input ```n```

Output:
![image](https://user-images.githubusercontent.com/45442467/141992857-bee45bf1-29e4-4b59-8797-a0ed925bad47.png)



![image](https://user-images.githubusercontent.com/45442467/141992026-3b94eaf5-df31-415f-a0c1-a0a16a4d7258.png)
