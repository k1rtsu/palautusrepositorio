from matchers import And, All, Or, Not, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, qu = All()):
        self.build_q = qu

    def build(self):
        return self.build_q
    
    def plays_in(self, team):
        return QueryBuilder(And(self.build_q, PlaysIn(team)))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.build_q, HasAtLeast(value, attr)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.build_q, HasFewerThan(value, attr)))
    
    def one_of(self, m1, m2):
        return QueryBuilder(Or(m1, m2))
