############################################################
from typing import TypeVar, Generic
from collections.abc import Callable
############################################################

#alias
nint = int
#alias
sint = int

############################################################

XS = TypeVar('XS')
X0 = TypeVar('X0')

class fngseq(Generic[XS,X0]):

    def nilq(self, xs: XS) -> bool:
        return self.forall(xs, lambda _: False)

    def foritm(self, xs: XS, work: Callable[[X0], None]) -> None:
        raise NotImplementedError
    def iforitm(self, xs: XS, work: Callable[[nint, X0], None]) -> None:
        raise NotImplementedError

    def forall(self, xs: XS, test: Callable[[X0], bool]) -> bool:
        raise NotImplementedError
    def iforall(self, xs: XS, test: Callable[[nint, X0], bool]) -> bool:
        raise NotImplementedError

# end of [class class fngseq(Generic[XS,X0]):...]

############################################################
