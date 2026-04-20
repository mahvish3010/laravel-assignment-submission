<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

// Calendar route for Task 2
Route::get('/calendar', function () {
    return view('calendar');
})->name('calendar');