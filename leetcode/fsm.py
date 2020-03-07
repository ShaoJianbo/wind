# -*- coding:utf8 -*-


class FsmState(object):
    """状态机基类"""
    def enter(self, event, fsm):
        """event为触发状态转换的事件-->进入状态的操作"""
        pass

    def exit(self, fsm):
        """离开状态-->离开状态的操作"""
        pass


class DvdPowerOn(FsmState):
    def enter(self, event, fsm):
        print("dvd is power on")


class DvdPlaying(FsmState):
    def enter(self, event, fsm):
        print("dvd is going to play")

    def exit(self, fsm):
        print("dvd stoped play")


class DvdPausing(FsmState):
    def enter(self, event, fsm):
        print("dvd is going to pause")

    def exit(self, fsm):
        print("dvd stopped pause")


class DvdPowerOff(FsmState):
    def enter(self, event, fsm):
        print("dvd is power off")


class FsmEvent(object):
    pass


class PowerOnEvent(FsmEvent):
    pass


class PowerOffEvent(FsmEvent):
    pass


class PlayEvent(FsmEvent):
    pass


class PauseEvent(FsmEvent):
    pass

