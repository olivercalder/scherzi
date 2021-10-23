(define before-n
  (lambda (array n)
    (if (or (<= n 0) (null? array))
      '()
      (cons (car array) (before-n (cdr array) (- n 1))))))

(define after-n
  (lambda (array n)
    (cond ((<= n 0) array)
          ((null? array) '())
          (else (after-n (cdr array) (- n 1))))))

(define merge
  (lambda (left right)
    (cond ((null? left) right)
          ((null? right) left)
          ((< (car left) (car right))
            (cons (car left) (merge (cdr left) right)))
          (else
            (cons (car right) (merge left (cdr right)))))))

(define merge-sort
  (lambda (array)
    (if (<= (length array) 1) array
      (let ((middle (inexact->exact (floor (/ (length array) 2)))))
        (merge
          (merge-sort (before-n array middle))
          (merge-sort (after-n array middle)))))))

(define unsorted '(5 3 4 9 8 1 7 2 0 6))

(display unsorted)
(display "\n")
(display (merge-sort unsorted))
(display "\n")
