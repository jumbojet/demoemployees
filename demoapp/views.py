from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from demoapp.models import Employee
import os, sys ,datetime , pdb , json, time, datetime    


def get_all_employees(request):

    employees_list = Employee.objects.all()
    return render_to_response('Employee.html',{'employees_list':employees_list})


def get_employee_by_id(request):
    empDetail ={}
    if 'EMP_ID' in request.GET:
        emp_id = request.GET['EMP_ID']
        emp = Employee.objects.get(employeeid=emp_id)
        empDetail['EMPLOYEE_ID'] = emp.employeeid
        empDetail['EMPLOYEE_NAME'] = emp.name
        empDetail['EMPLOYEE_DOB'] =str(emp.dob.date()) # Get only the date part
        empDetail['EMPLOYEE_SALARY'] =emp.salary
    return HttpResponse(json.dumps(empDetail))

def get_employee_search(request):
    emp_id,emp_name ="",""
    empDetail ={}
    if 'EMP_ID' in request.GET:
        emp_id = request.GET['EMP_ID']
    if 'EMP_NAME' in request.GET:
        emp_name = request.GET['EMP_NAME']
    if emp_id == "":
        empSet = Employee.objects.filter(name=emp_name) # as there will be a list of employees with same name
        empList =[]
        for emp in empSet:
            empDict ={}
            empDict['EMPLOYEE_ID'] = emp.employeeid
            empDict['EMPLOYEE_NAME'] = emp.name
            empDict['EMPLOYEE_DOB'] =str(emp.dob.date()) # Get only the date part
            empDict['EMPLOYEE_SALARY'] =emp.salary
            empList.append(empDict)
        return HttpResponse(json.dumps(empList))
    emp = Employee.objects.get(employeeid=emp_id)
    empDetail['EMPLOYEE_ID'] = emp.employeeid
    empDetail['EMPLOYEE_NAME'] = emp.name
    empDetail['EMPLOYEE_DOB'] =str(emp.dob.date()) # Get only the date part
    empDetail['EMPLOYEE_SALARY'] =emp.salary
    return HttpResponse(json.dumps(empDetail))


