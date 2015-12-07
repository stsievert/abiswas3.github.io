import sys

with open('students') as f:
    a = f.readlines()

j = 0
projects = []
for i in xrange(0, len(a)):
    projects.append(j)
    j = (j+1) % 16

f = open('assignment.html', 'w')
sys.stdout = f

print '<!DOCTYPE html>'
print '<html>'
print '<head>'
print '<style>'
print 'table, th, td {'
print '    border: 1px solid black;'
print '    border-collapse: collapse;'
print '}'

print 'th, td {'
print 'padding: 5px;'
print '}'
print '</style>'
print '</head>'
print '<body>'

print '<table style="width:100%">'
print '<tr>'
print '    <th>%s</th>'%('Name')
print '    <th>%s</th>'%('Lab Number')
print '</tr>'

for i,j in zip(a, projects):
    print '<tr>'
    print '    <td>%s</td>'%(i)
    print '    <td>%d</td>'%(int(j)+1)
    print '</tr>'

print '</table>'

print '</body>'
print '</html>'
f.close()
