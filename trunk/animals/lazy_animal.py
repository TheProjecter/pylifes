# coding: utf-8
from lifebase import Animal, engine
from random import randrange

class LazyAnimal(Animal):
    '''
    just find and follow another animal within sight.
    ��������ͣ�����Լ���Ұ��Χ��һ���ж��������Ұ��Χ��������ȥ��ֱ������Ϊֹ��
    '''
    def initialize(self):
        self.color = 'blue'
        self.animal = None #��ǰ���ڸ��ٵĶ���
        self.trac('initializing')
        self.sprite_name = 'light'

    def on_idle(self):
        if not self.ismoving:
            if self.animal:
                self.follow()
            else:
                self.follow_another()
        else:
            temp = self.scanfor(self.follow)
            if not temp:
                self.trac('lost %s' % str(self.follow.name))
                self.stop_moving('lost target')
            else:
                pos = temp.position
                pos += (temp.v[0],temp.v[1])
                self.trac('target:%s;distance:%d;speed:(%d, %d)' % (temp.name, self.distance, self.velocity, temp.velocity))
                self.reset_target(pos)

    def on_move_completed(self,sender,args):
        self.trac('stopped for %s' % args.reason)

    def follow_another(self):
        '���ӣ�����ж��������Ұ��������ȥ�������Լ���'
        lifes = [ l for l in self.scan() if not isinstance(l, LazyAnimal) ]
        #print 'lazy scaned',len(lifes)
        if lifes:
            self.trac('scaned %d lifes ' % len(lifes))
            self.follow = lifes[0]
            self.trac('follow the first one %s (%d, %d)' % (self.follow.name,self.follow.position[0],self.follow.position[1]))
            self.begin_moving(self.follow.position)

    def follow(self):
        '���Ը��ٵ�ǰ�������Ѹ�������Ѱ����������'
        temp = self.scanfor(self.follow)
        if not temp:
            self.follow_another()
        else:
            pos = temp.position
            pos += (temp.v.x,temp.v.y)
            self.begin_moving(pos)


def make_animals():
    return [LazyAnimal(name='lazy%d' % i,
                    position=(randrange(engine.world_width),randrange(engine.world_height)),
                    maxv=7,
                    sight=60)
               for i in xrange(100)]
