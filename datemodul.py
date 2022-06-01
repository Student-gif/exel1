from calendar import month
import datetime

weeknum = {
1-4:1,
6-11:2,
13-18:3,
20-25:4, 
27-2:5,
4-9:6,
11-16:7, 
18-23:8, 
25-30:9,
1-6:10,
8-13:11,
15-20:12, 
22-27:13,
29-4:14,
6-11:15,
13-18:16,    
20-25:17,
27-1:18,
3-8:19,
10-15:20,
17-22:21, 
24-29:22, 
31-5:23, 
7-12:24, 
14-19:25, 
21-26:26, 
28-5:27, 
7-12:28, 
14-19:29, 
21-26:30, 
28-2:31, 
4-9:32,
11-16:33, 
18-23:34,
25-30:35, 
2-7:36, 
9-14:37, 
16-21:38, 
23-28:39, 
30-4:40,
6-11:41,
13-18:42, 
20-25:43, 
27-2:44, 
4-9:45, 
11-16:46, 
18-23:47, 
23-3:48}
septembary= {1:1,2:1,3:1,4:1,6:2,7:2,8:2,9:2,10:2,11:2,13:3,14:3,15:3,16:3,17:3,18:3,20:4,21:4,22:4,23:4,24:4,25:4,27:5,28:5,29:5,30:5}
octobory= {1:5,2:5,4:6,5:6,7:6,8:6,9:6,11:7,12:7,13:7,14:7,15:7,16:7,18:8,19:8,20:8,21:8,22:8,23:8,25:9,26:9,27:9,28:9,30:9}
november={
    1:10,
    2:10,
    3:10,
    4:10,
    5:10,
    6:10,
    8:11,
    9:11,
    10:11,
    11:11,
    12:11,
    13:11,
    15:12,
    16:12,
    17:12,
    18:12,
    19:12,
    20:12,
    22:13,
    23:13,
    24:13,
    25:13,
    26:13,
    27:13,
    28:14,
    29:14,
    30:14,
}
december={
    1:14,
    2:14,
    3:14,
    4:14,
    6:15,
    7:15,
    8:15,
    9:15,
    10:15,
    11:15,
    13:16,
    14:16,
    15:16,
    16:16,
    17:16,
    18:16,
    20:17,
    21:17,
    22:17,
    23:17,
    24:17,
    25:17,
    27:18,
    28:18,
    29:18,
    30:18,
    31:18,
}
january={1:18,
3:19,
4:19,
5:19,
6:19,
7:19,
8:19,
10:20,
11:20,
12:20,
13:20,
14:20,
15:20,
17:21,
18:21,
19:21,
20:21,
21:21,
22:21,
24:22,
25:22,
26:22,
27:22,
28:22,
29:22,
31:23
}
febrary={
1:23,
2:23,
3:23,
4:23,
5:23,
7:24,
8:24,
9:24,
10:24,
11:24,
12:24,
14:25,
15:25,
16:25,
17:25,
18:25,
19:25,
21:26,
22:26,
23:26,
24:26,
25:26,
26:26,
28:27,
29:27,
}
febraryreverse={
    23:1,
    23:2,
    23:3,
    23:4,
    23:5,
    24:7,
    24:8,
    24:9,
    24:10,
    24:11,
    24:12,
    25:14,
    25:15,
    25:16,
    25:17,
    25:18,
    25:19,
    26:21,
    26:22,
    26:23,
    26:24,
    26:25,
    26:26,
    27:28,
    27:29,
}
march = {
1:27,
2:27,
3:27,
4:27,
5:27,
7:28,
8:28,
9:28,
10:28,
11:28,
12:28,
14:29,
15:29,
16:29,
17:29,
18:29,
19:29,
21:30,
22:30,
23:30,
24:30,
25:30,
26:30,
28:31,
29:31,
30:31,
31:31,
}
april = {
    1:31,
    2:31,
    4:32,
    5:32,
    6:32,
    7:32,
    8:32,
    9:32,
    11:33,
    12:33,
    13:33,
    14:33,
    15:33,
    16:33,
    18:34,
    19:34,
    20:34,
    21:34,
    22:34,
    23:34,
    25:35,
    26:35,
    27:35,
    28:35,
    29:35,
    30:35,
}
may = {
    2:36,
    3:36,
    4:36,
    5:36,
    6:36,
    7:36,
    9:37,
    10:37,
    11:37,
    12:37,
    13:37,
    14:37,
    16:38,
    17:38,
    18:38,
    19:38,
    20:38,
    21:38,
    23:39,
    24:39,
    25:39,
    26:39,
    27:39,
    28:39,
    30:40,
    31:40
}
june = {
    1:40,
    2:40,
    3:40,
    4:40,
    6:41,
    7:41,
    8:41,
    9:41,
    10:41,
    11:41,
    13:42,
    14:42,
    15:42,
    16:42,
    17:42,
    18:42,
    20:43,
    21:43,
    22:43,
    23:43,
    24:43,
    25:43,
    27:44,
    28:44,
    29:44,
    30:44,
}
july = {
    1:44,
    2:44,
    4:45,
    5:45,
    6:45,
    7:45,
    8:45,
    9:45,
    11:46,
    12:46,
    13:46,
    14:46,
    15:46,
    16:46,
    18:47,
    19:47,
    20:47,
    21:47,
    22:47,
    23:47,
    24:48,
    25:48,
    26:48,
    27:48,
    28:48,
    29:48,
    30:48,
}
Month = {
    9:septembary,
    10:octobory,
    11:november,
    12:december,
    1:january,
    2:febrary,
    3:march,
    4:april,
    5:may,
    6:june,
    7:july,
}

daytime=datetime.date.today()
mm=datetime.date.today().month

m = Month[mm]
try:weeknum = m[daytime.day]
except:
    weeknum = march[daytime.day+1] 
    pass      