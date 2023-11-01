import { Inject, Injectable, inject } from '@angular/core';
import { ActivatedRouteSnapshot, RouterStateSnapshot, Router, CanActivateFn } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { AuthenticationService } from './authentication.service';

export const canActivate: CanActivateFn = (route: ActivatedRouteSnapshot, state: RouterStateSnapshot) => {
  if(inject(AuthenticationService).isAuthenticated())
  {
    if (route.url.toString().includes('search') && inject(CookieService).get('userType') === 'tutor') {
      inject(Router).navigate(['']);
      return false;
    }
    return true;
  }
  else
  {
    inject(Router).navigate(['']);
    return false;
  }
}
