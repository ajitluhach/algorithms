from eulertour import EulerTour


class BinaryEulerTour():
    """Abstract base class for performing euler tour of a binary tree.

    This version includes an additional _hook_invisit which is called after
    the visit to the left subtree (if any), yet before the visit to the
    right subtree (if any)

    Note: right child is always assigned index one even if no left child is
    there
    """
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self.tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(self, p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self.tree.right(p), d+1, path)
            path.pop()
        answer = self._hook._postvisit(self, p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        pass

