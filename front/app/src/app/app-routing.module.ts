import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { ProfileComponent } from './profile/profile.component';
import { AppointmentsComponent } from './appointments/appointments.component';
import { SearchComponent } from './search/search.component';
import { canActivate } from './auth.guard';
import { DuoComponent } from './duo/duo.component';

const routes: Routes = [
  {path: '', component: LandingPageComponent},
  {path: 'login/:userType', component: LoginComponent},
  {path: 'signup/:userType', component: SignUpComponent},
  {path: 'profile/:tutorId', component: ProfileComponent, canActivate: [canActivate]},
  {path: 'appointments', component: AppointmentsComponent, canActivate: [canActivate]},
  {path: 'search', component: SearchComponent, canActivate: [canActivate]},
  {path: 'search/:searchString', component: SearchComponent, canActivate: [canActivate]},
  {path: 'duo/:userType', component: DuoComponent},
  {path: '**', component: LandingPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
