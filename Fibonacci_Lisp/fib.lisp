(defun fib (n)
  (car (make_fib_array n)))

;;;TODO: do it without let* (and let)
(defun make_fib_array (n)
  (if (<= n 1)
      (list 1 1)
      (let* ((fib (make_fib_array (- n 1)))
	     (n1 (car fib))
	     (n2 (car (cdr fib))))
	(cons (+ n1 n2) fib))))

(defun for (start stop)
  (if (<= start stop)
      (cons start (for (+ start 1) stop))
      nil))

;;; compare with fib
(defun fibo_slow (n)
  (if (<= n 1)
      1
      (+ (fibo_slow (- n 1)) (fibo_slow (- n 2)))))
