## GRAPH JAPeTo FORMAT

GT-RR-GGGG-NNN is a plain text file format that contains graph representation.

```
G: Graph
```
```
T: Type, this can be Directed (D), Non-Directed (N) or Weighted (P)
```
```
RR: Representation this can be adjacency matrix (MA), adjacency list (LA) or incidence matrix (MI)
```
```
GGGG: file group to which it belongs 0000 - 9999
```
NNN: file identification
```
within the file any line starting with (#) will be a comment and should not considered.
