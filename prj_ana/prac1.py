{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1.0.1'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.__version__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "피자    17000\n",
      "치킨    18000\n",
      "콜라     1000\n",
      "맥주     5000\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "sr = pd.Series([17000, 18000, 1000, 5000],\n",
    "              index=[\"피자\", \"치킨\", \"콜라\", \"맥주\"])\n",
    "print(sr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[17000 18000  1000  5000]\n"
     ]
    }
   ],
   "source": [
    "print(sr.values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['피자', '치킨', '콜라', '맥주'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(sr.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       A  B  C\n",
      "one    1  2  3\n",
      "two    4  5  6\n",
      "three  7  8  9\n"
     ]
    }
   ],
   "source": [
    "values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n",
    "index = ['one', 'two', 'three']\n",
    "columns = ['A', 'B', 'C']\n",
    "\n",
    "df = pd.DataFrame(values, index=index, columns=columns)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       A  B  C\n",
      "one    1  2  3\n",
      "two    4  5  6\n",
      "three  7  8  9\n"
     ]
    }
   ],
   "source": [
    "val = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n",
    "idx = ['one', 'two', 'three']\n",
    "col = ['A', 'B', 'C']\n",
    "\n",
    "df = pd.DataFrame(val, index=idx, columns=col)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = [\n",
    "    ['1000', 'Steve', 90.72], \n",
    "    ['1001', 'James', 78.09], \n",
    "    ['1002', 'Doyeon', 98.43], \n",
    "    ['1003', 'Jane', 64.19], \n",
    "    ['1004', 'Pilwoong', 81.30],\n",
    "    ['1005', 'Tony', 99.14],\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      0         1      2\n",
      "0  1000     Steve  90.72\n",
      "1  1001     James  78.09\n",
      "2  1002    Doyeon  98.43\n",
      "3  1003      Jane  64.19\n",
      "4  1004  Pilwoong  81.30\n",
      "5  1005      Tony  99.14\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data, columns=[\"학번\", \"이름\", \"점수\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     학번        이름     점수\n",
      "0  1000     Steve  90.72\n",
      "1  1001     James  78.09\n",
      "2  1002    Doyeon  98.43\n",
      "3  1003      Jane  64.19\n",
      "4  1004  Pilwoong  81.30\n",
      "5  1005      Tony  99.14\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data, index=[\"0번\", \"1번\", \"2번\", \"3번\", \"4번\", \"5번\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       0         1      2\n",
      "0번  1000     Steve  90.72\n",
      "1번  1001     James  78.09\n",
      "2번  1002    Doyeon  98.43\n",
      "3번  1003      Jane  64.19\n",
      "4번  1004  Pilwoong  81.30\n",
      "5번  1005      Tony  99.14\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = { '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],\n",
    "'이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],\n",
    "         '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     학번        이름     점수\n",
      "0  1000     Steve  90.72\n",
      "1  1001     James  78.09\n",
      "2  1002    Doyeon  98.43\n",
      "3  1003      Jane  64.19\n",
      "4  1004  Pilwoong  81.30\n",
      "5  1005      Tony  99.14\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>학번</th>\n",
       "      <th>이름</th>\n",
       "      <th>점수</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>Steve</td>\n",
       "      <td>90.72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>James</td>\n",
       "      <td>78.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1002</td>\n",
       "      <td>Doyeon</td>\n",
       "      <td>98.43</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     학번      이름     점수\n",
       "0  1000   Steve  90.72\n",
       "1  1001   James  78.09\n",
       "2  1002  Doyeon  98.43"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>학번</th>\n",
       "      <th>이름</th>\n",
       "      <th>점수</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>Steve</td>\n",
       "      <td>90.72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>James</td>\n",
       "      <td>78.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1002</td>\n",
       "      <td>Doyeon</td>\n",
       "      <td>98.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1003</td>\n",
       "      <td>Jane</td>\n",
       "      <td>64.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1004</td>\n",
       "      <td>Pilwoong</td>\n",
       "      <td>81.30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     학번        이름     점수\n",
       "0  1000     Steve  90.72\n",
       "1  1001     James  78.09\n",
       "2  1002    Doyeon  98.43\n",
       "3  1003      Jane  64.19\n",
       "4  1004  Pilwoong  81.30"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1000\n",
       "1    1001\n",
       "2    1002\n",
       "3    1003\n",
       "4    1004\n",
       "5    1005\n",
       "Name: 학번, dtype: object"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"학번\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>학번</th>\n",
       "      <th>이름</th>\n",
       "      <th>점수</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>James</td>\n",
       "      <td>78.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1002</td>\n",
       "      <td>Doyeon</td>\n",
       "      <td>98.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1003</td>\n",
       "      <td>Jane</td>\n",
       "      <td>64.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1004</td>\n",
       "      <td>Pilwoong</td>\n",
       "      <td>81.30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1005</td>\n",
       "      <td>Tony</td>\n",
       "      <td>99.14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     학번        이름     점수\n",
       "1  1001     James  78.09\n",
       "2  1002    Doyeon  98.43\n",
       "3  1003      Jane  64.19\n",
       "4  1004  Pilwoong  81.30\n",
       "5  1005      Tony  99.14"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'np' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-26-e24177884c36>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ma\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mzeros\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'np' is not defined"
     ]
    }
   ],
   "source": [
    "a = np.zeros((2,3))\n",
    "print(a)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
