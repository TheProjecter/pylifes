version 0.1

this program have used some resources fetched through network: the images, tilemap.py. thank you, the authors !

requires:
  pygame: http://www.pygame.org/download.shtml
  StacklessPython: http://www.stackless.com/

You can execute TestAnimal.py to watch the demo.
If you don't like the gui interface , you can execute "TextAnimal.py -q" to run it quietly, then you can have a look at the interesting logs.
You can write your own animals.

the APIs provided for writing animals :

 * begin_moving( (int, int) ), stop_moving, reset_target( (int, int) )
 * scan() => list of AnimalStats , scanfor( AnimalStat ) => AnimalStat or None

enjoy yourself!

chinese doc:

ʹ�õ����µ�������͹��ߣ�
  pygame�����http://www.pygame.org/download.shtml�������°汾�� 
  StacklessPython�����http://www.stackless.com/������Ӧ�汾, ֱ�ӽ�stacklesspython�ṩ��python24.dll�ŵ�python��װĿ¼�£������ָ���׼python����stacklesspython��python24.dllɾ�����������, ����ֱ�Ӳ���frame��c�������⣬stackless��CPython��ȫ���ݣ����������ʹ�á�

ִ�� TestAnimal.py �ۿ�demo��
�޸� TestAnimal.py ��д�Լ���Animal��

ִ�� setup.py py2exe ����ִ�� ToExe.lnk ��ط�ʽ���Դ�����ִ���ļ���

 * �ṩAPI��begin_moving ��stop_moving���û����Ա�д�������Զ���Ĳ��Խ����ƶ���
 * �ṩAPI��scan ��scanfor���û���д�Ķ�����Թ۲���Ұ��Χ�ڵ��������ִ����Ӧ����Ϊ��

ʵ���˹�����ͼ!

enjoy yourself!
