import asyncio
import functools
import sys
from abc import ABC
from functools import wraps
from inspect import Parameter as InspectParameter, isclass, signature
from typing import Any, Callable, Dict, NewType, Tuple, Type, TypeVar, Union, ForwardRef, Optional  # type: ignore

from typing_extensions import Protocol

from .container import di, Container
from .errors import ExecutionError

T = TypeVar("T")
S = TypeVar("S")

ServiceDefinition = Union[Type[S], Callable]
ServiceResult = Union[S, Callable]


Undefined = NewType("Undefined", int)


class _ProtocolInit(Protocol):
    pass


_no_init = _ProtocolInit.__init__


def _resolve_forward_reference(module: Any, ref: Union[str, ForwardRef]) -> Any:
    pass


class Parameter:
    type: Any
    name: str
    default: Any

    def __init__(self, name: str, type: Any = Any, default: Any = Undefined):
        self.name = name
        self.type = type
        self.default = default


def _inspect_function_arguments(
    function: Callable,
) -> Tuple[Tuple[str, ...], Dict[str, Parameter]]:
    pass


def _resolve_function_kwargs(
    alias_map: Dict[str, str],
    parameters_name: Tuple[str, ...],
    parameters: Dict[str, Parameter],
    container: Container,
) -> Dict[str, Any]:
    pass


def _decorate(binding: Dict[str, Any], service: ServiceDefinition, container: Container) -> ServiceResult:

    # ignore abstract class initialiser and protocol initialisers
    pass


def inject(
    _service: Optional[ServiceDefinition] = None,
    alias: Optional[Any] = None,
    bind: Optional[Dict[str, Any]] = None,
    container: Container = di,
    use_factory: bool = False,
) -> Union[ServiceResult, Callable[[ServiceDefinition], ServiceResult]]:
    pass


__all__ = ["inject"]
