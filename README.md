<div class="form-group row">
        <label for="username" class="col-md-4 col-form-label text-md-right">{{ __('Password') }}</label>
        <div class="col-md-6">
            <input id="email" type="email" class="form-control{{ $errors->has('email') ? ' is-invalid' : '' }}" name="email" value="{{ old('email') }}" required>

            @if ($errors->has('email'))
                <span class="invalid-feedback" role="alert">
                  <strong>{{ $errors->first('email') }}</strong>
              </span>
            @endif
        </div>
    </div>

nrdtweeting
===========

It's just simple update status and send a direct message on twitter. This code written in python and using Mike Verdone (sixohsix) --> https://github.com/sixohsix/twitter/tree/master. 

For the tutorial please visit my blog: http://nordskriving.wordpress.com/2014/03/25/update-status-twitter-menggunakan-python/ Written in Bahasa Indonesia)
