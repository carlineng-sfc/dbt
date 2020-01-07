from typing import List
from hologram.helpers import StrEnum


class NodeType(StrEnum):
    Model = 'model'
    Analysis = 'analysis'
    Test = 'test'
    Snapshot = 'snapshot'
    Operation = 'operation'
    Seed = 'seed'
    RPCCall = 'rpc'
    Documentation = 'docs'
    Source = 'source'
    Macro = 'macro'

    @classmethod
    def executable(cls) -> List['NodeType']:
        return [
            cls.Model,
            cls.Test,
            cls.Snapshot,
            cls.Analysis,
            cls.Operation,
            cls.Seed,
            cls.Documentation,
            cls.RPCCall,
        ]

    @classmethod
    def refable(cls) -> List['NodeType']:
        return [
            cls.Model,
            cls.Seed,
            cls.Snapshot,
        ]


class RunHookType(StrEnum):
    Start = 'on-run-start'
    End = 'on-run-end'
