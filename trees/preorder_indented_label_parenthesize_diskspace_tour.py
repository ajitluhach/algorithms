from eulertour import EulerTour


class PreorderPrintIndentTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*' ' + str(p.element))

# Use tour = PreorderPrintIndentTour(T)
# tour.execute()

class PreorderPrintIndentedLabel(EulerTour):
    def _hook_postvisit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)
        print(2*d*' ' + label + str(p.element()))


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:  # p follows a sibling
            print(',', end='')  # preface with comma
        print(p.element(), end='')  # pprint the element itself 
        if not self.tree().is_leaf(p):  # if p has children
            print(' (', end='')  # print opening parenthesis

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):  # if p has children
            print(')', end='')  # print closing parenthesis


class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, result):
        # we simply add space associated with p to it's subtrees.
        return p.element().space() + sum(results)
    

