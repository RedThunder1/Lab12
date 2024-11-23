class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        """Toggles tv's power."""
        self.__status = not self.__status

    def mute(self):
        """Toggles if the tv is muted"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """Raises tv's channel up 1, if it is at the max channel it goes to min channel"""
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """Raises tv's channel down 1, if it is at the min channel it goes to max channel"""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """Raises tv's volume 1, if it reaches max it does not raise past"""
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Lowers tv's volume 1, if it reaches min it does not lower past"""
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Method to show tv statsu
        :return: tv status
        """
        volume = self.__volume if not self.__muted else 0
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'