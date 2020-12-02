function workon
if count $argv > /dev/null
vf activate $argv
else
vf ls
end
end
