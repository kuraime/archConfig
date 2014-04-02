(require 'package)
(add-to-list 'package-archives
             '("marmalade" . "http://marmalade-repo.org/packages/"))
(package-initialize)


; GHCi interaction
(require 'inf-haskell)
(setq haskell-program-name "ghci")

(defun my-load-and-switch ()
  "Make \C-c\C-z switch to inferior buffer and load the Haskell file."
  (interactive)
  (inferior-haskell-load-file)
  (switch-to-haskell))

; /etc/emacs/site-start.d/50haskell-mode.el loads haskell-indentation by default
(remove-hook 'haskell-mode-hook 'turn-on-haskell-indentation)

(defun my-haskell-common-mode-hook ()
  (turn-on-auto-fill)
  (turn-on-haskell-indent)
  (setq haskell-indent-offset 2))

(defun my-haskell-mode-hook ()
  (define-key haskell-mode-map "\C-c\C-n"  'goto-line)
  (define-key haskell-mode-map "\C-c;"     'comment-region)
  (define-key haskell-mode-map "\C-u\C-c;" 'uncomment-region)
  (define-key haskell-mode-map "\C-c\C-z"  'my-load-and-switch))


(add-hook 'haskell-mode-hook 'my-haskell-common-mode-hook)
(add-hook 'haskell-mode-hook 'my-haskell-mode-hook)

(defun my-literate-haskell-mode-hook ()
  (define-key literate-haskell-mode-map "\C-c\C-n"  'goto-line)
  (define-key literate-haskell-mode-map "\C-c;"     'comment-region)
  (define-key literate-haskell-mode-map "\C-u\C-c;" 'uncomment-region)
  (define-key literate-haskell-mode-map "\C-c\C-z"  'my-load-and-switch))

(add-hook 'literate-haskell-mode-hook 'my-haskell-common-mode-hook)
(add-hook 'literate-haskell-mode-hook 'my-literate-haskell-mode-hook)


(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes (quote (wombat))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;; (require 'coffeemode)
(require 'package)
(add-to-list 'package-archives
             '("melpa" . "http://melpa.milkbox.net/packages/") t)

(global-set-key (kbd "C-x g") 'magit-status)
(global-set-key (kbd "C-c r") 'query-replace-regexp)

(setq auto-save-timeout 60)
(setq read-file-name-completion-ignore-case 't)
(setq-default indent-tabs-mode nil)
(setq tab-width 4)
(setq require-final-newline 't)
(show-paren-mode 1)

